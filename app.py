from flask import Flask, request, render_template
import sklearn
import pickle
import pandas as pd
import numpy as np
import jsonify
import requests
from datetime import datetime

app = Flask(__name__)
model = pickle.load(open('car_rf.pkl','rb'))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods = ["GET", "POST"])
def predict():
    if request.method == "POST":
        
        # Year of Registration
        Year = int(request.form["Year"])
        
        # Kilometers Dirven
        Kilometers_Driven = int(request.form["Kilometers_Driven"])
        
        # Owner Type
        Owner_Type = int(request.form["Owner_Type"])
        
        # Seats
        Seats = int(request.form["Seats"])
        
        # Power
        Power = round(float(request.form["Power(bhp)"]), 2)
        
        # Mileage
        Mileage = round(float(request.form["Mileage(km/kg)"]), 2)
        
        # Engine Capacity
        Engine = round(float(request.form["Engine(CC)"]), 2)
        
        # Location
        # Ahemdabad = 0 (not in column)
        Location = request.form["Location"]
        if(Location == 'Mumbai'):
            Mumbai = 1
            Pune = 0
            Chennai = 0
            Coimbatore = 0
            Hyderabad = 0
            Jaipur = 0
            Kochi = 0
            Kolkata = 0
            Delhi = 0
            Bangalore = 0
            
        elif(Location == 'Pune'):
            Mumbai = 0
            Pune = 1
            Chennai = 0
            Coimbatore = 0
            Hyderabad = 0
            Jaipur = 0
            Kochi = 0
            Kolkata = 0
            Delhi = 0
            Bangalore = 0
        
        elif(Location == 'Chennai'):
            Mumbai = 0
            Pune = 0
            Chennai = 1
            Coimbatore = 0
            Hyderabad = 0
            Jaipur = 0
            Kochi = 0
            Kolkata = 0
            Delhi = 0
            Bangalore = 0
        
        elif(Location == 'Coimbatore'):
            Mumbai = 0
            Pune = 0
            Chennai = 0
            Coimbatore = 1
            Hyderabad = 0
            Jaipur = 0
            Kochi = 0
            Kolkata = 0
            Delhi = 0
            Bangalore = 0
        
        elif(Location == 'Hyderabad'):
            Mumbai = 0
            Pune = 0
            Chennai = 0
            Coimbatore = 0
            Hyderabad = 1
            Jaipur = 0
            Kochi = 0
            Kolkata = 0
            Delhi = 0
            Bangalore = 0
            
        elif(Location == 'Jaipur'):
            Mumbai = 0
            Pune = 0
            Chennai = 0
            Coimbatore = 0
            Hyderabad = 0
            Jaipur = 1
            Kochi = 0
            Kolkata = 0
            Delhi = 0
            Bangalore = 0
            
        elif(Location == 'Kochi'):
            Mumbai = 0
            Pune = 0
            Chennai = 0
            Coimbatore = 0
            Hyderabad = 0
            Jaipur = 0
            Kochi = 1
            Kolkata = 0
            Delhi = 0
            Bangalore = 0
            
        elif(Location == 'Kolkata'):
            Mumbai = 0
            Pune = 0
            Chennai = 0
            Coimbatore = 0
            Hyderabad = 0
            Jaipur = 0
            Kochi = 0
            Kolkata = 1
            Delhi = 0
            Bangalore = 0
            
        elif(Location == 'Delhi'):
            Mumbai = 0
            Pune = 0
            Chennai = 0
            Coimbatore = 0
            Hyderabad = 0
            Jaipur = 0
            Kochi = 0
            Kolkata = 0
            Delhi = 1
            Bangalore = 0
            
        elif(Location == 'Bangalore'):
            Mumbai = 0
            Pune = 0
            Chennai = 0
            Coimbatore = 0
            Hyderabad = 0
            Jaipur = 0
            Kochi = 0
            Kolkata = 0
            Delhi = 0
            Bangalore = 1
            
        else:
            Mumbai = 0
            Pune = 0
            Chennai = 0
            Coimbatore = 0
            Hyderabad = 0
            Jaipur = 0
            Kochi = 0
            Kolkata = 0
            Delhi = 0
            Bangalore = 0
            
        # Fueltype
        # Cng is 0
        Fuel_Type = request.form["Fuel_Type"]
        if(Fuel_Type == "Petrol"):
            Petrol = 1
            Diesel = 0
            LPG = 0
        
        elif(Fuel_Type == "Diesel"):
            Petrol = 0
            Diesel = 1
            LPG = 0
            
        elif(Fuel_Type == "LPG"):
            Petrol = 0
            Diesel = 0
            LPG = 1
            
        else:
            Petrol = 0
            Diesel = 0
            LPG = 0
            
        # Transmission
        # Automatic is 0
        Transmissionns = request.form["Transmission"]
        if(Transmissionns == "Manual"):
            Manual = 1
            
        else:
            Manual = 0
            
        #['Year', 'Kilometers_Driven', 'Owner_Type', 'Seats', 'Price',
        #'Power(bhp)', 'Mileage(km/kg)', 'Engine(CC)', 'Location_Bangalore',
       # 'Location_Chennai', 'Location_Coimbatore', 'Location_Delhi',
       #'Location_Hyderabad', 'Location_Jaipur', 'Location_Kochi',
       #'Location_Kolkata', 'Location_Mumbai', 'Location_Pune',
       #'Fuel_Type_Diesel', 'Fuel_Type_LPG', 'Fuel_Type_Petrol',
       #'Transmission_Manual'
        
        
        
        
        
        
        prediction = model.predict([[
            Year,
            Kilometers_Driven,
            Owner_Type,
            Seats,
            Power,
            Mileage,
            Engine,
            Bangalore,
            Chennai,
            Coimbatore,
            Delhi,
            Hyderabad,
            Jaipur,
            Kochi,
            Kolkata,
            Mumbai,
            Pune,
            Diesel,
            LPG,
            Petrol,
            Manual]])
            
        output = round(prediction[0], 2)
        if output<0:
            return render_template('index.html', prediction_texts = "Something is wrong please fill proper input!!")
        else:
            return render_template('index.html', prediction_text = "Price of the car is Rs. {} lakh".format(output))
    else:
        return render_template('index.html')
            
if __name__=="__main__":
    app.run(debug=True)