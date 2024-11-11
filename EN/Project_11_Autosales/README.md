# Calculation the price of cars for the "Not Damaged, Not Painted" Service

## Project Description
The "Not Damaged, Not Painted" service for selling used cars with mileage is developing an application to attract new customers. In it, you can find out the market value of your car. **It is necessary to build a model** that can determine this value. We have data on technical characteristics, equipment and prices of other cars.

The customer's criteria are:
- quality of prediction;
- time for training the model;
- prediction time of the model.
 
Note:  
- for evaluating the quality of models we apply the RMSE metric,
- the RMSE metric value should be less than 2500.

## Data Description
Data is in the autos.csv file and includes features:
- DateCrawled — date of downloading the questionnaire from the base
- VehicleType — type of car body
- RegistrationYear — year of registration of the vehicle
- Gearbox — type of transmission
- Power — power (hp)
- Model — car model
- Kilometer — mileage (km)
- RegistrationMonth — month of registration of the vehicle
- FuelType — fuel type
- Brand — car brand
- Repaired — whether the machine was in repair or not
- DateCreated — date of creating the questionnaire
- NumberOfPictures — number of car photos
- PostalCode — postal code of the user (user) who created the questionnaire
- LastSeen — date of last user activity

Target feature
Price — price (euros)

Specific steps for analyzing and predicting data are listed in the notebook text.

In this project, the following aspects of the topic **Numerical Methods** have been worked out:
- Analysis of algorithms for applying numerical methods
- Gradient descent
- Training with gradient descent
- Gradient boosting
- Patterns for solving tasks