from flask import Flask,render_template,request,redirect
from models.models import EdinetCodeInfo
from models.models import FinanceInfo
from models.models import Stocks
from decimal import Decimal, ROUND_HALF_UP

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    title = request.args.get("title")
    all_edinetcodeinfo = EdinetCodeInfo.query.all()
    return render_template("index.html",title=title,all_edinetcodeinfo=all_edinetcodeinfo)

@app.route("/type")
def type():
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
    all_stocks = Stocks.query.filter(Stocks.code==code).all()
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
    
    return render_template("result.html",title=code,all_edinetcodeinfo=all_edinetcodeinfo, all_financeinfo=all_financeinfo, all_stocks=all_stocks)

if __name__ == "__main__":
    app.run(debug=True)