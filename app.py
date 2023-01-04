#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from flask import Flask, render_template
DEVELOPMENT_ENV  = True

app = Flask(__name__)
 
with open('test.json') as f:
  data = json.load(f)
countries=list(data["Countries"].keys())
customers=data["Customers"]

#Run app by -  flask --app app.py --debug run
# Customize your font and color here +Please be confirm this given font  is  added on index.html from googl font  or  other source os also ok  , Such as i added Roboto  font  in header ( Link ) .
headerBG='#07004d'
font="Roboto"
detailsBG="#8080804a"
summaryBG="#8080804a"



@app.route('/')
def index():  
  return render_template('index.html', summaryBG=summaryBG, headerBG=headerBG,detailsBG=detailsBG,font=font, data=data,countries=countries,customers=customers)

if __name__ == '__main__':
    app.run(debug=DEVELOPMENT_ENV)