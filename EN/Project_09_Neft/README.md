# Profit Forecasting for the Oil Company "GlavRosGosNeft"

## Project Description
Assuming we are working in the oil company "GlavRosGosNeft", we need to decide where to drill a new well. 
Typical steps for choosing a location are:
- In the chosen region, collect characteristics for wells: oil quality and volume of its reserves;
- Build a model for predicting the volume of reserves in new wells;
- Choose wells with the highest rated values;
- Determine the region with the maximum total profit from selected wells.

We have been provided with oil samples in three regions. Characteristics for each well in the region are already known. **You need to build a model** for determining the region where extraction will bring the highest profit. And then analyze the possible profit and risks using the Bootstrap technique.

## Data Description
Data on geological exploration of three regions are located in files: geo_data_0.csv, geo_data_1.csv, geo_data_2.csv, data for each region are similar:
- id — unique identifier of the well;
- f0, f1, f2 — three characteristics of points (it doesn't matter what they mean, but the features themselves are significant);
- product — volume of reserves in the well (thousand barrels).

Task conditions:
- Only linear regression is suitable for training the model. 
- When prospecting a region, 500 points are explored, and using machine learning, 200 best ones are selected for development. 
- The budget for developing wells in the region is 10 billion rubles.
- At current prices, one barrel of raw material brings 450 rubles of income. Income from each unit of product is 450 thousand rubles, since the volume is specified in thousands of barrels.
- After assessing risks, only those regions should be left where the probability of losses is less than 2.5%. Among them, choose the region with the highest average profit.

The data are synthetic: contract details and site characteristics are not disclosed.

Specific steps for analyzing data are presented in the notebook text.  

In this project, the following aspects of the topic **Machine Learning in Business** have been worked out:
- Application of ML in business tasks, business metrics
- Connections between product metrics and ML indicators
- Launching new functionality
- Collecting data
- Behavioral algorithms