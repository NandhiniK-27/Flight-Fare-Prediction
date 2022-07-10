#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import numpy as np
import pickle
import datetime as dt
from sklearn.preprocessing import LabelEncoder
from lightgbm import LGBMRegressor
import gzip, pickle, pickletools

#Load in model
with gzip.open('lgbm.pickle', 'rb') as f:
    p = pickle.Unpickler(f)
    load_clf = p.load()
    
st.header("Flight Fare Prediction")

dict1 = {'B': 0, 'E': 1 ,'PE': 2}
dict2 = {'Amritsar' : 0, 'Bagdogra' : 1, 'Bengaluru' : 2, 'Bhubaneswar' : 3 , 'Chandigarh':4 , 'Chennai' :5 , 'Coimbatore':6 , 'Goa' : 7 , 'Guwahati' : 8, 'Hyderabad' : 9, 'Indore' : 10 , 'Jaipur' : 11 , 'Kochi' : 12  , 'Kolkata' : 13 , 'Kozhikode' :14 , 'Lucknow':15 , 'Mangalore':16 , 'Mumbai':17 , 'Nagpur' :18 , 'New Delhi':19 , 'Patna':20 , 'Port Blair' :21 , 'Pune': 22 , 'Raipur': 23 , 'Ranchi':24 , 'Srinagar': 25 , 'Thiruvananthapuram' : 26 ,'Tiruchirappalli' :27 ,'Varanasi' : 28 , 'Visakhapatnam': 29 }
dict3 = {'Air India' : 0 ,'Air India, AirAsia' : 1 ,'Air India, Go Air' :2 ,'Air India, IndiGo' : 3,
 'Air India, Spicejet' : 4 ,'Air India,Vistara' : 5,'AirAsia' : 6,'AirAsia, Air India' : 7,
 'AirAsia, Go Air' : 8 ,'AirAsia, IndiGo' : 9,'AirAsia, Spicejet' : 10,
 'AirAsia, Vistara' : 11 ,'Go Air' : 12, 'Go Air, Air India' : 13, 'Go Air, AirAsia' : 14,
 'Go Air, IndiGo' : 15, 'Go Air, Spicejet' : 16 ,'Go Air, Vistara' : 17, 'IndiGo' : 18,
 'IndiGo, Air India' : 19, 'IndiGo, Air Asia' : 20 ,'IndiGo, Go Air' : 21, 'IndiGo, Spicejet' : 22,
 'IndiGo, TruJet' : 23 ,'IndiGo, Vistara' : 24 ,'Spicejet' : 25  ,'Spicejet, Air India' :26,
 'Spicejet, Air Asia' : 27 ,'Spicejet, Go Air' : 28, 'Spicejet, IndiGo' : 29,
 'Spicejet, Vistara' :30 ,'TruJet, IndiGo' : 31 ,'TruJet, Vistara' : 32 ,'Vistara' : 33,
 'Vistara, Air India' : 34,'Vistara AirAsia' :35,'Vistara, Go Air' : 36,
 'Vistara, IndiGo' : 37 ,'Vistara, Spicejet' : 38, 'flybig, Vistara': 39 ,'flybig, Air India': 40,
 'flybig, Go Air' : 41 , 'flybig, IndiGo' : 42, 'flybig, Spicejet' : 43,'flybig, Vistara': 44}
        
Airline = st.selectbox('Airline',({'Air India' : 0 ,'Air India, AirAsia' : 1 ,'Air India, Go Air' :2 ,'Air India, IndiGo' : 3,
 'Air India, Spicejet' : 4 ,'Air India,Vistara' : 5,'AirAsia' : 6,'AirAsia, Air India' : 7,
 'AirAsia, Go Air' : 8 ,'AirAsia, IndiGo' : 9,'AirAsia, Spicejet' : 10,
 'AirAsia, Vistara' : 11 ,'Go Air' : 12, 'Go Air, Air India' : 13, 'Go Air, AirAsia' : 14,
 'Go Air, IndiGo' : 15, 'Go Air, Spicejet' : 16 ,'Go Air, Vistara' : 17, 'IndiGo' : 18,
 'IndiGo, Air India' : 19, 'IndiGo, Air Asia' : 20 ,'IndiGo, Go Air' : 21, 'IndiGo, Spicejet' : 22,
 'IndiGo, TruJet' : 23 ,'IndiGo, Vistara' : 24 ,'Spicejet' : 25  ,'Spicejet, Air India' :26,
 'Spicejet, Air Asia' : 27 ,'Spicejet, Go Air' : 28, 'Spicejet, IndiGo' : 29,
 'Spicejet, Vistara' :30 ,'TruJet, IndiGo' : 31 ,'TruJet, Vistara' : 32 ,'Vistara' : 33,
 'Vistara, Air India' : 34,'Vistara AirAsia' :35,'Vistara, Go Air' : 36,
 'Vistara, IndiGo' : 37 ,'Vistara, Spicejet' : 38, 'flybig, Vistara': 39 ,'flybig, Air India': 40,
 'flybig, Go Air' : 41 , 'flybig, IndiGo' : 42, 'flybig, Spicejet' : 43,'flybig, Vistara': 44}))
    
Cabin = st.radio('Cabin', ({'B': 0, 'E': 1 ,'PE': 2}))
Dept_date = st.date_input("Departure Date", dt.date(2022, 7, 1))
Dept_city = st.selectbox('Departure City',({'Amritsar' : 0, 'Bagdogra' : 1, 'Bengaluru' : 2, 'Bhubaneswar' : 3 , 'Chandigarh':4 , 'Chennai' :5 , 'Coimbatore':6 , 'Goa' : 7 , 'Guwahati' : 8, 'Hyderabad' : 9, 'Indore' : 10 , 'Jaipur' : 11 , 'Kochi' : 12  , 'Kolkata' : 13 , 'Kozhikode' :14 , 'Lucknow':15 , 'Mangalore':16 , 'Mumbai':17 , 'Nagpur' :18 , 'New Delhi':19 , 'Patna':20 , 'Port Blair' :21 , 'Pune': 22 , 'Raipur': 23 , 'Ranchi':24 , 'Srinagar': 25 , 'Thiruvananthapuram' : 26 ,'Tiruchirappalli' :27 ,'Varanasi' : 28 , 'Visakhapatnam': 29 }))
arrival_city = st.selectbox('Arrival City',({'Amritsar' : 0, 'Bagdogra' : 1, 'Bengaluru' : 2, 'Bhubaneswar' : 3 , 'Chandigarh':4 , 'Chennai' :5 , 'Coimbatore':6 , 'Goa' : 7 , 'Guwahati' : 8, 'Hyderabad' : 9, 'Indore' : 10 , 'Jaipur' : 11 , 'Kochi' : 12  , 'Kolkata' : 13 , 'Kozhikode' :14 , 'Lucknow':15 , 'Mangalore':16 , 'Mumbai':17 , 'Nagpur' :18 , 'New Delhi':19 , 'Patna':20 , 'Port Blair' :21 , 'Pune': 22 , 'Raipur': 23 , 'Ranchi':24 , 'Srinagar': 25 , 'Thiruvananthapuram' : 26 ,'Tiruchirappalli' :27 ,'Varanasi' : 28 , 'Visakhapatnam': 29 }))   
dept_hours = st.slider('Departure Hours', 0, 23, 0)
Passenger = st.slider('No.Of.Passenger',1,20,1)

airline = dict3[Airline]
cabin = dict1[Cabin]
dept_city = dict2[Dept_city]
arr_city = dict2[arrival_city]
optimal_time = abs(dept_hours - 4)
weekday = Dept_date.weekday()
passenger = abs(Passenger)


d = [airline, cabin, dept_city, arr_city, optimal_time, weekday]
data = np.asarray(d)

if st.button('Predict'):
    st.write('fare Predicting')
    prediction = load_clf.predict(data.reshape(1,-1).astype(float))

    st.write('Flight Fare is',passenger*prediction)
else:
    st.write('Click the predict button')

    st.write("Built by Nandhini K")

