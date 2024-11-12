# Taxi Orders Forecasting

## Project Description
The "Clear Taxi" company has collected historical data on taxi orders at airports. To attract more drivers during peak hours, it is necessary to forecast the number of taxi orders for the next hour. It is required **to build a model** for this prediction.

The value of the RMSE metric on the test sample must not exceed 48.

## Data Description
The data is located in the taxi.csv file and represents a time series with the number of taxi orders by 20-minute intervals.
The number of orders is located in the 'num_orders' column.

Specific steps for analysis and forecasting of data are provided in the notebook text.

In this project, the following aspects of the topic **Time Series** have been worked out:
- Introduction to time series analysis (trend search and seasonality detection)
- Time series data preprocessing
- Creating table features from time series data
- Applying regression models to time series and specialized models (SARIMA) 
- Forecasting time series