import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('CVD_prediction_final_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    
    age = int(request.form['age'])
    diabetes = str(request.form['diabetes'])
    hypertension = str(request.form['hypertension'])
    smoking = str(request.form['smoking'])
    family = str(request.form['family'])
    
    inp_df = pd.DataFrame([[age, diabetes, hypertension, smoking, family]],
                                       columns=['age', 'diabetes_cat', 'sysbp_cat',
                                                'smoking_cat', 'family_history_cat'])
    
    to_scale = ['age']
    not_to_scale = ['family_history_cat', 'diabetes_cat', 'smoking_cat', 'sysbp_cat']
    
    scaled_val = pd.DataFrame(scaler.transform(np.array(inp_df[to_scale]).reshape(-1,1)),
                          columns=['age']).reset_index(drop=True)
    
    risk_input = pd.concat([scaled_val, inp_df[not_to_scale].reset_index(drop=True)], axis=1)
    
    prediction = model.predict_proba(risk_input)[:,1]

    return render_template('index.html', prediction_text='Your risk of developing cardiovascular disease is {}%'.format(int(prediction*100)))

if __name__ == "__main__":
    app.run(debug=True)


   