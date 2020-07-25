from flask import Flask,render_template,request,redirect,jsonify,abort,make_response
from flask_cors import CORS
from models.models import EdinetCodeInfo
from models.models import FinanceInfo
from decimal import Decimal, ROUND_HALF_UP
from google.cloud import datastore
from pytrends.request import TrendReq
import json

app = Flask(__name__)
btd = {'1': '水産・農林業', '2': '鉱業', '3': '建設業', '4': '食料品', '5': '繊維製品', '6': 'パルプ・紙', '7': '化学',
       '8': '医薬品', '9': '石油・石炭製品', '11': 'ゴム製品', '12': 'ガラス・土石製品', '13': '鉄鋼', '14': '非鉄金属',
       '15': '金属製品', '16': '機械', '17': '電気機器', '18': '輸送用機器', '19': '精密機器', '20': 'その他製品', '21': '電気・ガス業',
       '22': '陸運業', '23': '海運業', '24': '空運業', '25': '倉庫・運輸関連', '26': '情報・通信業', '27': '卸売業', '28': '小売業',
       '29': '銀行業', '30': '証券、商品先物取引業', '31': '保険業', '32': 'その他金融業', '33': '不動産業', '34': 'サービス業'}

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html",)
    
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/buisnesstype/<btype>")
def buisnesstype(btype):
    all_edinetcodeinfo = EdinetCodeInfo.query.filter(EdinetCodeInfo.businesstype==btd[btype]).all()
    return render_template("buisnesstype.html",all_edinetcodeinfo=all_edinetcodeinfo)

@app.route("/search",methods=['GET'])
def search():
    code = "/company/" + request.args.get("code","")
    return redirect(code)

@app.route('/company/<code>')
def get_finance(code):
    all_edinetcodeinfo = EdinetCodeInfo.query.filter(EdinetCodeInfo.securitiescode==code).all()
    
    all_financeinfo = FinanceInfo.query.filter(FinanceInfo.securitiescode==code).all()
    for financeinfo in all_financeinfo:
        # netsales
        if len(str(financeinfo.netsales)) == 0:
            financeinfo.netsales = '-'
        else:
            tmp = financeinfo.netsales / 1000000
            financeinfo.netsales = Decimal(str(tmp)).quantize(Decimal('0'),    rounding=ROUND_HALF_UP)
            
        # costofsales
        if len(str(financeinfo.costofsales)) == 0:
            financeinfo.costofsales = '-'
        else:
            tmp = financeinfo.costofsales / 1000000
            financeinfo.costofsales = Decimal(str(tmp)).quantize(Decimal('0'),    rounding=ROUND_HALF_UP)
            
        # grossprofit
        if len(str(financeinfo.grossprofit)) == 0:
            financeinfo.grossprofit = '-'
        else:
            tmp = financeinfo.grossprofit / 1000000
            financeinfo.grossprofit = Decimal(str(tmp)).quantize(Decimal('0'),    rounding=ROUND_HALF_UP)
            
        # sellinggeneral
        if len(str(financeinfo.sellinggeneral)) == 0:
            financeinfo.sellinggeneral = '-'
        else:
            tmp = financeinfo.sellinggeneral / 1000000
            financeinfo.sellinggeneral = Decimal(str(tmp)).quantize(Decimal('0'),    rounding=ROUND_HALF_UP)
            
        # operatingincome
        if len(str(financeinfo.operatingincome)) == 0:
            financeinfo.operatingincome = '-'
        else:
            tmp = financeinfo.operatingincome / 1000000
            financeinfo.operatingincome = Decimal(str(tmp)).quantize(Decimal('0'),    rounding=ROUND_HALF_UP)
            
        # nonoperatingincome
        if len(str(financeinfo.nonoperatingincome)) == 0:
            financeinfo.nonoperatingincome = '-'
        else:
            tmp = financeinfo.nonoperatingincome / 1000000
            financeinfo.nonoperatingincome = Decimal(str(tmp)).quantize(Decimal('0'),    rounding=ROUND_HALF_UP)
            
        # nonoperatingexpenses
        if len(str(financeinfo.nonoperatingexpenses)) == 0:
            financeinfo.nonoperatingexpenses = '-'
        else:
            tmp = financeinfo.nonoperatingexpenses / 1000000
            financeinfo.nonoperatingexpenses = Decimal(str(tmp)).quantize(Decimal('0'),    rounding=ROUND_HALF_UP)
            
        # ordinaryIncome
        if len(str(financeinfo.ordinaryincome)) == 0:
            financeinfo.ordinaryincome = '-'
        else:
            tmp = financeinfo.ordinaryincome / 1000000
            financeinfo.ordinaryincome = Decimal(str(tmp)).quantize(Decimal('0'),    rounding=ROUND_HALF_UP)
            
        # extraordinaryincome
        if len(str(financeinfo.extraordinaryincome)) == 0:
            financeinfo.extraordinaryincome = '-'
        else:
            tmp = financeinfo.extraordinaryincome / 1000000
            financeinfo.extraordinaryincome = Decimal(str(tmp)).quantize(Decimal('0'),    rounding=ROUND_HALF_UP)
            
        # extraordinaryloss
        if len(str(financeinfo.extraordinaryloss)) == 0:
            financeinfo.extraordinaryloss = '-'
        else:
            tmp = financeinfo.extraordinaryloss / 1000000
            financeinfo.extraordinaryloss = Decimal(str(tmp)).quantize(Decimal('0'),    rounding=ROUND_HALF_UP)
            
        # incomebeforeincometaxes
        if len(str(financeinfo.incomebeforeincometaxes)) == 0:
            financeinfo.incomebeforeincometaxes = '-'
        else:
            tmp = financeinfo.incomebeforeincometaxes / 1000000
            financeinfo.incomebeforeincometaxes = Decimal(str(tmp)).quantize(Decimal('0'),    rounding=ROUND_HALF_UP)
            
        # incometaxes
        if len(str(financeinfo.incometaxes)) == 0:
            financeinfo.incometaxes = '-'
        else:
            tmp = financeinfo.incometaxes / 1000000
            financeinfo.incometaxes = Decimal(str(tmp)).quantize(Decimal('0'),    rounding=ROUND_HALF_UP)
            
        # profitloss
        if len(str(financeinfo.profitloss)) == 0:
            financeinfo.profitloss = '-'
        else:
            tmp = financeinfo.profitloss / 1000000
            financeinfo.profitloss = Decimal(str(tmp)).quantize(Decimal('0'),    rounding=ROUND_HALF_UP)
            
        # currentassets
        if len(str(financeinfo.currentassets)) == 0:
            financeinfo.currentassets = '-'
        else:
            tmp = financeinfo.currentassets / 1000000
            financeinfo.currentassets = Decimal(str(tmp)).quantize(Decimal('0'),    rounding=ROUND_HALF_UP)
            
        # noncurrentassets
        if len(str(financeinfo.noncurrentassets)) == 0:
            financeinfo.noncurrentassets = '-'
        else:
            tmp = financeinfo.noncurrentassets / 1000000
            financeinfo.noncurrentassets = Decimal(str(tmp)).quantize(Decimal('0'),    rounding=ROUND_HALF_UP)
            
        # propertyplantandequipment
        if len(str(financeinfo.propertyplantandequipment)) == 0:
            financeinfo.propertyplantandequipment = '-'
        else:
            tmp = financeinfo.propertyplantandequipment / 1000000
            financeinfo.propertyplantandequipment = Decimal(str(tmp)).quantize(Decimal('0'),    rounding=ROUND_HALF_UP)
            
        # intangibleassets
        if len(str(financeinfo.intangibleassets)) == 0:
            financeinfo.intangibleassets = '-'
        else:
            tmp = financeinfo.intangibleassets / 1000000
            financeinfo.intangibleassets = Decimal(str(tmp)).quantize(Decimal('0'),    rounding=ROUND_HALF_UP)
            
        # investmentsAndotherAssets
        if len(str(financeinfo.investmentsAndotherAssets)) == 0:
            financeinfo.investmentsAndotherAssets = '-'
        else:
            tmp = financeinfo.investmentsAndotherAssets / 1000000
            financeinfo.investmentsAndotherAssets = Decimal(str(tmp)).quantize(Decimal('0'),    rounding=ROUND_HALF_UP)
            
        # currentliabilities
        if len(str(financeinfo.currentliabilities)) == 0:
            financeinfo.currentliabilities = '-'
        else:
            tmp = financeinfo.currentliabilities / 1000000
            financeinfo.currentliabilities = Decimal(str(tmp)).quantize(Decimal('0'),    rounding=ROUND_HALF_UP)
            
        # noncurrentliabilities
        if len(str(financeinfo.noncurrentliabilities)) == 0:
            financeinfo.noncurrentliabilities = '-'
        else:
            tmp = financeinfo.noncurrentliabilities / 1000000
            financeinfo.noncurrentliabilities = Decimal(str(tmp)).quantize(Decimal('0'),    rounding=ROUND_HALF_UP)
            
        # netAssets
        if len(str(financeinfo.netAssets)) == 0:
            financeinfo.netAssets = '-'
        else:
            tmp = financeinfo.netAssets / 1000000
            financeinfo.netAssets = Decimal(str(tmp)).quantize(Decimal('0'),    rounding=ROUND_HALF_UP)
            
        # scf
        if len(str(financeinfo.scf)) == 0:
            financeinfo.scf = '-'
        else:
            tmp = financeinfo.scf / 1000000
            financeinfo.scf = Decimal(str(tmp)).quantize(Decimal('0'),    rounding=ROUND_HALF_UP)
            
        # icf
        if len(str(financeinfo.icf)) == 0:
            financeinfo.icf = '-'
        else:
            tmp = financeinfo.icf / 1000000
            financeinfo.icf = Decimal(str(tmp)).quantize(Decimal('0'),    rounding=ROUND_HALF_UP)
            
        # fcf
        if len(str(financeinfo.fcf)) == 0:
            financeinfo.fcf = '-'
        else:
            tmp = financeinfo.fcf / 1000000
            financeinfo.fcf = Decimal(str(tmp)).quantize(Decimal('0'),    rounding=ROUND_HALF_UP)
    
    return render_template("result.html",code=code,all_edinetcodeinfo=all_edinetcodeinfo, all_financeinfo=all_financeinfo)

@app.route('/stocks/<code>')
def get_stocks(code):
    all_edinetcodeinfo = EdinetCodeInfo.query.filter(EdinetCodeInfo.securitiescode==code).all()

    #datastore_client = datastore.Client.from_service_account_json('json file name')
    datastore_client = datastore.Client()
    key = datastore_client.key('Stocks',int(code))
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