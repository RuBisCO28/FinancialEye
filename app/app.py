from flask import Flask,render_template,request,redirect
from models.models import EdinetCodeInfo
from models.models import FinanceInfo

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    title = request.args.get("title")
    all_edinetcodeinfo = EdinetCodeInfo.query.all()
    return render_template("index.html",title=title,all_edinetcodeinfo=all_edinetcodeinfo)

@app.route("/search",methods=['GET'])
def get():
    code = "/company/" + request.args.get("code","")
    return redirect(code)

@app.route('/company/<code>')
def get_finance(code):
    all_edinetcodeinfo = EdinetCodeInfo.query.filter(EdinetCodeInfo.securitiescode==code).all()
    all_financeinfo = FinanceInfo.query.filter(FinanceInfo.securitiescode==code).all()
    for financeinfo in all_financeinfo:
        tmp = financeinfo.netsales / 1000000
        financeinfo.netsales = round(tmp)
    return render_template("result.html",title=code,all_edinetcodeinfo=all_edinetcodeinfo, all_financeinfo=all_financeinfo)

if __name__ == "__main__":
    app.run(debug=True)