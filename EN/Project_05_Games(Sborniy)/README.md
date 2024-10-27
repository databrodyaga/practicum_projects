# Analysis of Sales Patterns in Game Data from "StreamChick" Store.

## Project Description
You work at the online store “StreamChick”, which sells games all around the world. Available historical data on game sales, user and critic reviews, genres, and platforms (e.g., Xbox or PlayStation) are accessible through open sources. The task is to identify the key patterns of successful game sales. This would enable making an informed bet on a potentially popular product and planning advertising campaigns.  
The data available goes up until 2016. Assuming it's currently December 2016, you plan a campaign for 2017. It doesn’t matter whether your projections are based on the data from 2016 or even further in advance (e.g., 2026-2027). 
In the dataset, there is an abbreviation for ESRB (Entertainment Software Rating Board) — it’s an association that evaluates video game content and assigns a suitable age category, like “For adults”, “For children under the age of 7” or “For teenagers”.  

## Data Description
Name — game title  
Platform — platform of the game  
Year_of_Release — year released  
Genre — genre of the game  
NA_sales — sales in North America (millions sold)  
EU_sales — sales in Europe (millions sold)  
JP_sales — sales in Japan (millions sold)  
Other_sales — sales in other countries (millions sold)  
Critic_Score — critic review score (maximum 100)  
User_Score — user review score (maximum 10)  
Rating — ESRB rating (english for “Entertainment Software Rating Board”). This association defines game ratings and assigns a suitable age category.  
The data from the year 2016 might be incomplete.


## Tasks for Analysis
1. Create user profiles for each region: 
   - Determine the most popular platforms for each user in NA, EU, and JP (top-5). Describe differences in sales percentages.
   - Identify the top genres for users in each region (top-5) and explain their differences.
2. Is the ESRB rating a factor in sales of games in any specific region?  
3. Check the hypothesis: 
   - Are the average user review scores for Xbox One and PC platforms equal?
   - Are there significant differences between the average user review scores of Action and Sports genres.
4. Determine your own alpha threshold.

The analysis steps are outlined below, referring to the notes from a notebook.

In this project, preliminary data analysis skills were applied, hypotheses formulated, and tested.