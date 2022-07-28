from flask import Flask, render_template, redirect,url_for,request, flash,send_from_directory
from flask_bootstrap import Bootstrap
import requests
URL="http://www.boredapi.com/api/activity"
app = Flask(__name__)
Bootstrap(app)
form=[]
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
@app.route('/')
def home():
    info = requests.get(URL)
    form = info.json()
    print(form)
    form =form["activity"]

    return render_template("index.html", form=form)



if __name__=="__main__":
    app.run(debug=True)

