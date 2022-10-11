
from flask import Flask, render_template,jsonify,request
import pickle
import numpy as np


app=Flask(__name__)
model=pickle.load(open('model_decision.pkl','rb'))
@app.route('/',methods=['GET'])
def home():
    return render_template('web.html')

@app.route('/predict',methods=['POST'])

def predict():
    if request.method=='POST':
        gender=request.form['Gender']
        if gender=="Male":
            gender=1
        else:
            gender=0
        age=int(request.form["Age"])
        driving=request.form["Driving"]
        if driving=="Yes":
            driving=1
        else:
            driving=0
        insure=request.form['previos_insure']
        if insure=="Yes":
            insure=1
        else:
            insure=0
        vehicle_damage=request.form['Vehicle_damage']
        if vehicle_damage=="Yes":
            vehicle_damage=1
        else:
            vehicle_damage=0
        annual_prem=float(request.form['Annual_prem'])
        cust_vintage=int(request.form['Vintage_cust'])
        age_veh=request.form['Vehilce_age']
        if age_veh=="1 To 2 Years":
            Vehicle_Age_1_2_Year=1
            Vehicle_Age_lessthan_1_Year=0
            Vehicle_Age_gretaer_than_Years=0
        if age_veh=='Less than One Year':
            Vehicle_Age_1_2_Year=0
            Vehicle_Age_lessthan_1_Year=1
            Vehicle_Age_gretaer_than_Years=0
        else:
            Vehicle_Age_1_2_Year=0
            Vehicle_Age_lessthan_1_Year=0
            Vehicle_Age_gretaer_than_Years=1
        prediction=model.predict([[gender,age,driving,insure,vehicle_damage,annual_prem,cust_vintage,Vehicle_Age_1_2_Year,Vehicle_Age_lessthan_1_Year,Vehicle_Age_gretaer_than_Years]])
        out=int(prediction[0])
        if out==0:
            outp="Not Interested"
        elif out==1:
            outp="Interested"   
        return render_template('web.html',prediction_text="Customer is  {}.".format(outp))
    else:
        return render_template('web.html')

if __name__=="__main__":
    app.run(debug=True)   