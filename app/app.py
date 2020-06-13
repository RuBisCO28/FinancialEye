from flask import Flask,render_template,request
from models.models import EdinetCodeInfo

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    title = request.args.get("title")
    all_edinetcodeinfo = EdinetCodeInfo.query.all()
    return render_template("index.html",title=title,all_edinetcodeinfo=all_edinetcodeinfo)

@app.route("/result",methods=["post"])
def post():
    code = request.form["code"]
    all_edinetcodeinfo = EdinetCodeInfo.query.filter(EdinetCodeInfo.securitiescode==code).all()
    return render_template("result.html",title=code,all_edinetcodeinfo=all_edinetcodeinfo)

if __name__ == "__main__":
    app.run(debug=True)