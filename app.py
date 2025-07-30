import pickle

from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

## Import ridge regresor model and standard scaler pilkle

ridge_model = pickle.load(open(r"C:\Users\godar\OneDrive\Desktop\study material\Machine Learning\Regression\ML and to And project\model\ridge_regression.pkl",'rb'))
standard_scaler = pickle.load(open(r"C:\Users\godar\OneDrive\Desktop\study material\Machine Learning\Regression\ML and to And project\model\scaler.pkl",'rb'))

# Route for home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods= ['GET','POST'])
def predict_datapoint():
    if request.method=='POST':
        Temparature = float(request.form.get('Temparature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('WS'))
        Rain = float(request.form.get('Rain'))
        FFMS = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

        new_data_scaled = standard_scaler.transform([[Temparature,RH, Ws, Rain, FFMS, DMC, ISI, Classes, Region]])
        result = ridge_model.predict(new_data_scaled)


        return render_template('home.html', result=result[0])
    else:
        return render_template('home.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')