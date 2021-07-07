# -*- coding: utf-8 -*-

import numpy as np
#import pandas as pd
from flask import Flask, request, render_template
#import joblib
#from flask import redirect
import pickle

app=Flask(__name__,template_folder='templates')
model=pickle.load(open('PL.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')
# prediction function
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 10)
    loaded_model = pickle.load(open("PL.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    return result[0]
  
@app.route('/result', methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        result = ValuePredictor(to_predict_list)        
        if int(result)== 1:
            prediction ='Congratulations,there is high chances that you will Placed.'
        else:
            prediction ='You are lack in skills,We best of luck you to be ahead of yourself in terms skills.'            
        return render_template("result.html", prediction = prediction)

if __name__=='__main__':
    app.run(debug=True,use_reloader=False)