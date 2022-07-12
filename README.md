# Flight-Fare-Prediction
This is a Flight Fare prediction web-app, developed by Nandhini K. It predicts the prices of flight, based on the six inputs provided by you. Its prediction model is based on  lightGBM machine learning model, which has been trained on 300k+ historic flight Fare data.

## Problem Statement

Flight ticket prices can be something hard to guess, today it might see a price, check out the price of
the sameflight tomorrow, and it will be a different story.


To solve this problem, provide prices of flight tickets for various airlines between the before
departure hour and optimal hour between various cities, using which aim to build a model which
predicts the prices of the flights using various input features.


In this project going to use Python programming language to run the codes for our computational
purposes. And analyze different methods from the point of view of accuracy and propose an
integrated method to improve our prediction results.


![image](https://user-images.githubusercontent.com/90173983/178414704-63fbac76-c23a-4d0e-a12e-b13bdf8bcbda.png)


## Dataset

The model has been trained with a dataset having 14 attributes and over 3 million+ data points. 

• Price : The Price of the ticket.
• departure_time : The time when the journey starts from the city.
• arrival_time : Time of arrival at the destination.
• Airline : The name of the airline.
• Cabin : The section of an aircraft in which passengers travel.
• Dept_city : The departure city means from which the services begin.
• Dept_date : Date of the journey.
• arrival_city : The arrival city means from which the service end.
• stops : Total stops between the departure city and arrival city.
• duration : Total duration of the flight.
• weekday : Day of journey starts.
• dept_hours : The hour when the journey starts from the departure city.
• Dept_flights_time : The season of departure flight.
• optimal_hours : Before departure time buy a minimum flight price.

The model took only six parameters , same as input parameters, for final training as according to feature importance map, only these 6 parameters were found to useful.

## Model

The model LightGBM is decision tree based regression model , optimized with a gradient boosting method to enhance performance. The model used adam_optimizer as learning parameter* and learning_rate=0.01. It had 20,000 estimators. The max_depth parameter of decision tree was set to max_depth=8. It had an evaluation_metric as eval_metric=rmse.

Deployed Machine learning model(lightGBM) with an accuracy of over 87% for flight price prediction.

It takes six inputs from the user
 
Cabin - The section of an aircraft in which passengers travel.
Airline -  The name of the airline.
Dept_city - The departure city means from which the services begin.
Dept_date - the date of flight 
arrival_city - The arrival city means from which the service end.
Dept_hours (the approximate integer/ nearest integer to flight departure timing)

The output of the model is float point value of flight Price upto 4 decimal places.

**Note** : The internal model is based on a optimal_time parameter , which assumes that time of booking the flight is 4 hours before departure. So, according to model, the cheapest flight prices are 4 hours before actual flight takeoff. Please book your flights accordingly.

## Evaluation

We used mean_squared_error and mean_absolute_error for final evaluation of the model.

**Link to the website**

https://myflightappprediction.herokuapp.com/


![image](https://user-images.githubusercontent.com/90173983/178415183-4ba2b6e0-44f3-4ec1-9b12-da2dac38fe12.png)


**This project was the final part of Data Analyst Internship at Technocolabs Softwares Inc. **


