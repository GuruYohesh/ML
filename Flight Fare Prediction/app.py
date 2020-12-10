# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 07:57:10 2020

@author: KANNAN
"""

from flask import Flask, render_template, request
import pandas as pd
#import sklearn
import pickle

model = pickle.load(open("flight_rf.pkl", "rb"))

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('Airlines.html')

@app.route('/Predict', methods = ["GET", "POST"])

def Predict():
    if request.method == "POST":
        #Date of Journey
        # Departure DMY
        date_dep = request.form["Departure_Date"]
        Dep_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        Dep_month = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").month)
        Dep_year = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").year)
        # Departure Time
        Dep_hour = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").hour)
        Dep_minute = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").minute)
        
                
       
        date_arrival = request.form["Arrival_Date"]
        #Arrival DMY
        Arrival_day = int(pd.to_datetime(date_arrival, format="%Y-%m-%dT%H:%M").day)
        Arrival_month = int(pd.to_datetime(date_arrival, format="%Y-%m-%dT%H:%M").month)
        Arrival_year = int(pd.to_datetime(date_arrival, format="%Y-%m-%dT%H:%M").year)
        # Arrival Time            
        Arrival_hour = int(pd.to_datetime(date_arrival, format="%Y-%m-%dT%H:%M").hour)
        Arrival_minute = int(pd.to_datetime(date_arrival, format="%Y-%m-%dT%H:%M").minute)
        
        # Duration in hrs
        from datetime import datetime
        dep_date = datetime(Dep_year,Dep_month,Dep_day,Dep_hour,Dep_minute)
        arrival_date = datetime(Arrival_year,Arrival_month,Arrival_day,Arrival_hour,Arrival_minute)
        diff = arrival_date - dep_date
        t = pd.to_datetime(diff,format="%H:%M:%S")
        duration_hour = t.hour
        duration_minute = t.minute

                
        # Source
        source = request.form["Source"]
        if (source == 'New Delhi'):
            s_New_Delhi = 1
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0

        elif (source == 'Kolkata'):
            s_New_Delhi = 0
            s_Kolkata = 1
            s_Mumbai = 0
            s_Chennai = 0

        elif (source == 'Mumbai'):
            s_New_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 1
            s_Chennai = 0

        elif (source == 'Chennai'):
            s_New_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 1

        else:
            s_New_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0


        
        
        # Destination
        destination = request.form["Destination"]
        if (destination == 'Cochin'):
            d_Cochin = 1
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
        
        elif (destination == 'New Delhi'):
            d_Cochin = 0
            d_New_Delhi = 1
            d_Hyderabad = 0
            d_Kolkata = 0

        elif (destination == 'Hyderabad'):
            d_Cochin = 0
            d_New_Delhi = 0
            d_Hyderabad = 1
            d_Kolkata = 0

        elif (destination == 'Kolkata'):
            d_Cochin = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 1

        else:
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0

        # Airline
        airline = request.form["Airline"]

        if(airline=='Jet Airways'):
            Jet_Airways = 1
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 

        elif (airline=='IndiGo'):
            Jet_Airways = 0
            IndiGo = 1
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 

        elif (airline=='Air India'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 1
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
            
        elif (airline=='Multiple carriers'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 1
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
            
        elif (airline=='SpiceJet'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 1
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
            
        elif (airline=='Vistara'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 1
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airline=='GoAir'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 1
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airline=='Multiple carriers Premium economy'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 1
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airline=='Jet Airways Business'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 1
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airline=='Vistara Premium economy'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 1
            Trujet = 0
            
        elif (airline=='Trujet'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 1

        else:
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
        
        # Total_Stops
        stops = int(request.form["Total_Stops"])
        
        prediction=model.predict([[
            stops,
            Dep_day,
            Dep_month,
            Dep_hour,
            Dep_minute,
            Arrival_hour,
            Arrival_minute,
            duration_hour,
            duration_minute,
            Air_India,
            GoAir,
            IndiGo,
            Jet_Airways,
            Jet_Airways_Business,
            Multiple_carriers,
            Multiple_carriers_Premium_economy,
            SpiceJet,
            Trujet,
            Vistara,
            Vistara_Premium_economy,
            s_Chennai,
            s_Kolkata,
            s_Mumbai,
            s_New_Delhi,
            d_Cochin,
            d_Hyderabad,
            d_Kolkata,
            d_New_Delhi
        ]])
        
        output=round(prediction[0],2)

        
        return render_template('Airlines.html',prediction_text = "Your Flight Fare is {} INR".format(output)) 
    
    return render_template('Airlines.html')
    

if __name__ == '__main__':
    app.run()


