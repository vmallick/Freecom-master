from flask import Flask,render_template,request,Response
from price_comp import comp

import os
import pandas as pd
app=Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    try:
        return render_template("home.html")
    except:
        return render_template("error.html")

@app.route("/result",methods=['post', 'get'])
def result_page():
    try:
        if request.method=='POST':
            x=request.form.get('nm1')
            print(x)
            x_name=x

            cont=True
            while cont:
                try:
                    items=comp(x)
                    cont=False
                    
                except:
                    cont=True
        
        return render_template("result.html",items=items,x_name=x_name)
    except:
        return render_template("error.html")

@app.route("/price")
def price():
    try:
        return render_template("price_input.html")
    except:
        return render_template("error.html")

@app.route("/prod")
def product():
    try:
        return render_template("prod_input.html")
    except:
        return render_template("error.html")





@app.route('/redeem')
def redeem():
    return render_template("redeem.html")
    
@app.route('/qr')
def qr_disp():
    return "<h1>ToDo</h1>"

@app.route('/qrComp')
def qrComp_disp():
    return "<h1>ToDo</h1>"
#  for error
#  vanshita
@app.route('/error')
def error():
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)
