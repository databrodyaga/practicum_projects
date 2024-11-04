# Modeling Satisfaction Rate for Employee Turnover Prediction

## Project Description

HR analysts at the company "Careful Work" assist businesses in optimizing personnel management: the business provides data, and analysts suggest ways to avoid financial losses and employee attrition. Machine learning will be useful in helping HR analysts respond to business inquiries faster and more accurately.  
The company has provided data with various employee characteristics, including their job satisfaction level within the company. This information was gathered from feedback forms: employees fill out a questionnaire, and their satisfaction level is calculated as a proportion from 0 to 1, where 0 means completely dissatisfied, and 1 means fully satisfied.

The project includes several tasks:

The first task is to build a model that can predict an employee's satisfaction level based on client data.

The second task is to build a model that can predict whether an employee will leave the company based on client data.

## Data Description
**Task 1: Predicting Employee Satisfaction Level**  
For this task, the client provided data with the following features:
- `id` — unique employee identifier  
- `dept` — department in which the employee works  
- `level` — job level  
- `workload` — employee workload level  
- `employment_years` — tenure in the company (in years)  
- `last_year_promo` — indicates if there was a promotion in the past year  
- `last_year_violations` — indicates if the employee violated the employment contract in the past year  
- `supervisor_evaluation` — performance evaluation by the supervisor  
- `salary` — monthly salary of the employee  
- `job_satisfaction_rate` — employee’s satisfaction level with the company, the target variable.

**Task 2: Predicting Employee Turnover**  
For this task, the same input features as the previous task can be used. However, the target variable differs: it is `quit`, indicating employee turnover.

Specific steps for data analysis and target prediction are presented in the notebook text.  

This project addresses all **key aspects of solving predictive tasks using machine learning**—from data preprocessing and exploratory analysis to training and evaluating various models.