# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 11:20:09 2020

@author: KANNAN
"""


from flask import Flask, render_template, request
import emoji
#import sklearn
import pickle

model = pickle.load(open("diabetes_logreg.pkl", "rb"))

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('Diabetes.html')

@app.route('/predict', methods = ["GET", "POST"])

def Diabetes():
    if request.method == "POST":
        
        Glucose = float(request.form["Glucose"])
        if (Glucose > 0 and Glucose < 140):
            Glucose_Prediabetes = 0
            Glucose_Diabetes = 0
        elif(Glucose >= 140 and Glucose < 200):
            Glucose_Prediabetes = 1
            Glucose_Diabetes = 0
        else:
            Glucose_Prediabetes = 0
            Glucose_Diabetes = 1

       
        BloodPressure = float(request.form["BloodPressure"])  
        if (BloodPressure > 0 and BloodPressure < 80):
            BloodPressure_Hyper_St1 = 0
            BloodPressure_Hyper_St2 = 0
            BloodPressure_Hyper_Emer = 0
        elif (BloodPressure >=80 and BloodPressure < 90):
            BloodPressure_Hyper_St1 = 1
            BloodPressure_Hyper_St2 = 0
            BloodPressure_Hyper_Emer = 0
        elif (BloodPressure >= 90 and BloodPressure < 120):
            BloodPressure_Hyper_St1 = 0
            BloodPressure_Hyper_St2 = 1
            BloodPressure_Hyper_Emer = 0
        else:
            BloodPressure_Hyper_St1 = 0
            BloodPressure_Hyper_St2 = 0
            BloodPressure_Hyper_Emer = 1
        
        
        BMI = float(request.form["BMI"])
        if (BMI > 0 and BMI < 18.5):
            BMI_Normal = 0
            BMI_Overweight = 0
            BMI_Obese = 0
        elif (BMI >= 18.5 and BMI < 24.9):
            BMI_Normal = 1
            BMI_Overweight = 0
            BMI_Obese = 0
        elif (BMI >= 24.9 and BMI < 29.9):
            BMI_Normal = 0
            BMI_Overweight = 1
            BMI_Obese = 0
        else:
            BMI_Normal = 0
            BMI_Overweight = 0
            BMI_Obese = 1
        
        
        Insulin = float(request.form["Insulin"])
        if (Insulin >= 100 and Insulin <= 126):
            Insulin_Normal = 1
        else:
            Insulin_Normal = 0
        
                
        Pregnancies = float(request.form["Pregnancies"])
        Pregnancies = (Pregnancies - 3.874593) / 3.443637 
        
        
        SkinThickness = float(request.form["SkinThickness"])
        SkinThickness = (SkinThickness - 29.180782) / 8.94289800
        
        
        
        DiabetesPedigreeFunction = float(request.form["DiabetesPedigreeFunction"])
        DiabetesPedigreeFunction = (DiabetesPedigreeFunction - 0.466471) / 0.333203
        
        
        Age = float(request.form["Age"])
        Age = (Age - 33.594463) / 12.016168
        
        prediction = model.predict([[
            Pregnancies,
            SkinThickness,
            DiabetesPedigreeFunction,
            Age,
            BMI_Normal,
            BMI_Overweight,
            BMI_Obese,
            BloodPressure_Hyper_St1,
            BloodPressure_Hyper_St2,
            BloodPressure_Hyper_Emer,
            Glucose_Prediabetes,
            Glucose_Diabetes,
            Insulin_Normal
            ]])
       
        output = prediction[0]
        if output == 0:
            text = "You are Healthy!!"+"\U0001F603"
        else:
            text = "You have Diabetes"+"\U0001F61E"
                
        return render_template('Diabetes.html',prediction_text = text)  
   
    return render_template('Diabetes.html')
    

if __name__ == '__main__':
    app.run()
   