from flask import Flask,render_template,request,redirect,jsonify,abort,make_response
from flask_cors import CORS
from models.models import EdinetCodeInfo
from google.cloud import datastore
from google.cloud import storage
from io import BytesIO
from pytrends.request import TrendReq
import json
import pandas as pd

app = Flask(__name__)
btd = {'1': '水産・農林業', '2': '鉱業', '3': '建設業', '4': '食料品', '5': '繊維製品', '6': 'パルプ・紙', '7': '化学',
       '8': '医薬品', '9': '石油・石炭製品', '11': 'ゴム製品', '12': 'ガラス・土石製品', '13': '鉄鋼', '14': '非鉄金属',
       '15': '金属製品', '16': '機械', '17': '電気機器', '18': '輸送用機器', '19': '精密機器', '20': 'その他製品', '21': '電気・ガス業',
       '22': '陸運業', '23': '海運業', '24': '空運業', '25': '倉庫・運輸関連', '26': '情報・通信業', '27': '卸売業', '28': '小売業',
       '29': '銀行業', '30': '証券、商品先物取引業', '31': '保険業', '32': 'その他金融業', '33': '不動産業', '34': 'サービス業'}

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")
    
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/buisnesstype/<btype>")
def buisnesstype(btype):
    all_edinetcodeinfo = EdinetCodeInfo.query.filter(EdinetCodeInfo.businesstype==btd[btype]).all()
    return render_template("buisnesstype.html",all_edinetcodeinfo=all_edinetcodeinfo)

@app.route("/search",methods=['GET'])
def search():
    code = request.args.get("code","")
    if(code[0:4].isdigit()):
        url = "/company/" + code[0:4]
        return redirect(url)
    else:
        return render_template("404.html")

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html")

@app.route('/company/<code>')
def get_finance(code):
    all_edinetcodeinfo = EdinetCodeInfo.query.filter(EdinetCodeInfo.securitiescode==code).all()
    
    # for local
    #csv='archive/finance/'+str(code)+'.csv'
    #all_financeinfo = pd.read_csv(csv,header=None)
    
    # for GCP
    storage_client = storage.Client()
    bucket = storage_client.get_bucket('financeinfo')
    csv=str(code)+'.csv'
    blob = bucket.get_blob(csv)
    all_financeinfo = pd.read_csv(BytesIO(blob.download_as_string()),header=None)
    
    all_financeinfo.loc[:,4:27] /= 1000000
    all_financeinfo.loc[:,28] = (all_financeinfo.loc[:,6] / all_financeinfo.loc[:,4]) * 100
    all_financeinfo.loc[:,29] = (all_financeinfo.loc[:,8] / all_financeinfo.loc[:,4]) * 100
    all_financeinfo.loc[:,30] = (all_financeinfo.loc[:,11] / all_financeinfo.loc[:,4]) * 100
    all_financeinfo.loc[:,31] = (all_financeinfo.loc[:,16] / all_financeinfo.loc[:,4]) * 100
    all_financeinfo.fillna('',inplace=True)
    
    return render_template("result.html",code=code,all_edinetcodeinfo=all_edinetcodeinfo, all_financeinfo=all_financeinfo)

@app.route('/stocks/<code>')
def get_stocks(code):
    all_edinetcodeinfo = EdinetCodeInfo.query.filter(EdinetCodeInfo.securitiescode==code).all()

    # for local
    #datastore_client = datastore.Client.from_service_account_json('file.json')
    
    # for GCP
    datastore_client = datastore.Client()
    key = datastore_client.key('Stock',int(code))
    entity = datastore_client.get(key)
    result=entity.get("stock")
    all_stocks=result
    return render_template("stock.html",code=code,all_edinetcodeinfo=all_edinetcodeinfo, all_stocks=all_stocks)

@app.route('/gtrend/<code>')
def get_gtrend(code):
    all_edinetcodeinfo = EdinetCodeInfo.query.filter(EdinetCodeInfo.securitiescode==code).all()
    
    for edinetcodeinfo in all_edinetcodeinfo:
        gtrend = edinetcodeinfo.submitter.replace('株式会社','').replace('株','')
    pytrends = TrendReq(hl='ja-JP', tz=360)
    keyword=''.join(gtrend.split())
    kw_list = [keyword]
    pytrends.build_payload(kw_list, timeframe='today 1-m', geo='JP')
    df = pytrends.interest_over_time()
    dfi = df.drop("isPartial",axis=1)
    dt=[]
    for d in dfi.index.values:
        dt.append(str(d)[0:10])
    dfi['date'] = dt
    dfi.columns = ['name','date']
    
    trends = pytrends.related_queries()
    if(trends[keyword]['top'] is None):
        top = ['No data']
    else:
        top = trends[keyword]['top'].values.tolist()
    if(trends[keyword]['rising'] is None):
        rising = ['No data']
    else:
        rising = trends[keyword]['rising'].values.tolist()
    return render_template("gtrend.html",code=code,all_edinetcodeinfo=all_edinetcodeinfo, gtrend_g=dfi,gtrend_t=top,gtrend_r=rising)

if __name__ == "__main__":
    app.run(debug=True)