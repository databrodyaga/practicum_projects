# Prediction of milk yield for the dairy farm "Volny Lug"

## Project Description
We are an IT company that takes on custom machine learning projects. A farmer, the owner of the dairy farm "Volny Lug," approached us. He wants to purchase cows to expand his herd. For this purpose, he has secured a profitable contract with the "EcoFarm" pasture association.  
The contract allows the farmer to be very selective in choosing cows. He determines milk quality according to a strict methodology and needs to meet his dairy farm’s development plan. The farmer wants each cow to produce at least 6,000 kilograms of milk annually, and the milk must be tasty—strictly by his criteria, nothing less.  
Therefore, he requests a machine learning model to help manage risks and make objective purchasing decisions. "EcoFarm" is ready to provide detailed data on their cows. You are to create two predictive models for selecting cows for the herd:  
1. The first will predict a cow’s potential milk yield (target feature: Yield).
2. The second will estimate the likelihood of obtaining tasty milk from a cow (target feature: Milk Taste).

The model needs to select cows based on two criteria:  
- The average annual yield should be at least 6,000 kilograms;
- The milk must be tasty.

## Data Description
The data is presented in three datasets:  
- `ferma_main.csv`
- `ferma_dad.csv`
- `cow_buy.csv`

The **ferma_main.csv** file contains data on the farmer’s current herd:  
- `id` — unique identifier for each cow  
- `Удой, кг` — amount of milk the cow produces annually (in kilograms)  
- `ЭКЕ` (Energy Feed Unit) — a measure of the nutritional value of the cow’s feed  
- `Сырой протеин, г` — content of raw protein in the feed (in grams)  
- `СПО` (Sugar-Protein Ratio) — the ratio of sugar to protein in the cow’s feed  
- `Порода` — breed of the cow  
- `Тип пастбища` — type of pasture landscape where the cow grazed  
- `порода папы_быка` — breed of the cow's father  
- `Жирность,%` — fat content in the milk (in percentage)  
- `Белок,%` — protein content in the milk (in percentage)  
- `Вкус молока` — taste rating according to the farmer's personal criteria, binary feature (tasty, not tasty)  
- `Возраст` — age of the cow, binary feature (under_2_years, over_2_years)

Features in the `ferma_main.csv` dataset can be divided into groups:  
- Cow Characteristics:  id, Порода, порода папы_быка, Возраст;  
- Feed Characteristics: ЭКЕ (Энергетическая кормовая единица), Сырой протеин, г, СПО (Сахаро-протеиновое соотношение);
- Pasture Characteristic: Тип пастбища;  
- Milk Characteristics: Удой, кг, Жирность,%, Белок,%, Вкус молока.

The **ferma_dad.csv** file contains the names of the fathers of each cow in the farmer's herd:  
- `id` — unique identifier for each cow  
- `Имя Папы` — name of the cow's father

The **cow_buy.csv** file contains data on "EcoFarm" cows that the farmer wants to review before purchasing:  
- `Порода` — breed of the cow  
- `Тип пастбища` — type of pasture landscape where the cow grazed  
- `порода папы_быка` — breed of the cow's father  
- `Имя папы-быка` — name of the cow's father  
- `Текущая_жирность,%` — fat content in the milk (in percentage)  
- `Текущий_уровень_белок,%` — protein content in the milk (in percentage)  
- `Возраст` — age of the cow, binary feature (under_2_years, over_2_years)

The data in `ferma_main.csv` and `cow_buy.csv` is similar, but there are some differences in `cow_buy.csv`:  
- The protein and fat content in the milk is recorded at the time of sale — when "EcoFarm" provided their own feed for the cows.
- The feed parameters `ЭКЕ`, `Сырой протеин, г`, and `СПО` are absent. The customer's technologists have revised the feeding approach: values for each of these parameters are planned to increase by 5% for the new cows.  
- Additionally, the `Удой, кг` and `Вкус молока` features are missing. These are the target features to be predicted.

Detailed steps for data analysis are provided in the notebook text.

In this project, the following aspects of **Linear Models in Machine Learning** were covered:  
- Modeling and Machine Learning (the machine learning model creation cycle)  
- Linear Models and scikit-learn Library  
- Linear Algebra and the numpy Library  
- Regression and Classification Metrics  
- Hidden Model Errors  
- Modeling Scheme