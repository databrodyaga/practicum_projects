# Research of Apartment Sale Listings

## Project Description
We have access to data from the Yandex Real Estate service — an archive of apartment sale listings in St. Petersburg and nearby settlements over several years. We **need to learn** how to determine the market value of real estate objects. To do this, we will conduct an exploratory data analysis and establish the parameters that influence property prices. This will allow us to build an automated system: it will track anomalies and fraudulent activities.  
For each apartment for sale, there are two types of data available. The first is entered by the user, while the second is automatically obtained based on mapping data. For example, the distance to the center, airport, and other locations — this data is automatically retrieved from geoservices. The number of parks and bodies of water is also filled in without user involvement.

## Data Description
- airports_nearest — distance to the nearest airport in meters (m)  
- balcony — number of balconies  
- ceiling_height — ceiling height (m)  
- cityCenters_nearest — distance to the city center (m)  
- days_exposition — how many days the listing was posted (from publication to removal)  
- first_day_exposition — publication date  
- floor — floor  
- floors_total — total number of floors in the building  
- is_apartment — apartment (boolean type)  
- kitchen_area — kitchen area in square meters (m²)  
- last_price — price at the time of removal from publication  
- living_area — living area in square meters (m²)  
- locality_name — name of the settlement  
- open_plan — open-plan layout (boolean type)  
- parks_around3000 — number of parks within a radius of 3 km  
- parks_nearest — distance to the nearest park (m)  
- ponds_around3000 — number of bodies of water within a radius of 3 km  
- ponds_nearest — distance to the nearest body of water (m)  
- rooms — number of rooms  
- studio — studio apartment (boolean type)  
- total_area — total area of the apartment in square meters (m²)  
- total_images — number of photographs of the apartment in the listing  

The specific steps of the data analysis are outlined in the text of the notebook.  

In this project, the following aspects of **Exploratory Data Analysis** have been covered:  
- Introduction to exploratory data analysis (familiarization with the SciPy and Matplotlib libraries)  
- Initial graphs and conclusions  
- Studying data slices  
- Working with multiple data sources  
- Data interrelationships  
- Validation of results