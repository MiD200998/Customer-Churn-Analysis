from flask import Flask, request, render_template, url_for
from predict import value
app = Flask(__name__)

@app.route("/")
#def front():
#   return render_template("index.html")
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/formindex",methods=["POST"])
#def indexform():
#    category = request.form["category"]
#    rating = request.form["rating"]
#    skintype = request.form["skintype"]
#    return render_template("formindex.html",category=category,rating=rating,skintype=skintype)

@app.route("/formindex",methods=["POST"])
def output():
	form_data = request.form
	print(form_data)
	status = value(form_data)
    return render_template("response.html", status=status)
	InternationalPlan=request.form["InternationalPlan"]
#   VoiceMail=request.form["VoiceMail"]
#   TotalDayMinutes=request.form["TotalDayMinutes"]
#	TotalDayCharge=request.form["TotalDayCharge"]
#	TotalIntlCharge=request.form["TotalIntlCharge"]
#	CustomerServiceCalls=request.form["CustomerServiceCalls"]
#   form_data=request.form("category","rating","skintype")
#   status=value(InternationalPlan, VoiceMail, TotalDayMinutes, TotalDayCharge, TotalIntlCharge, CustomerServiceCalls)
if __name__ == "__main__":
    app.run(debug=True)
        