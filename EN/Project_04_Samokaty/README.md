# Statistical Data Analysis of the GoFast Scooter Rental Service  

## Project Description  
We have been provided with data on some users from various cities, as well as on their rides. We will analyze the data and test some hypotheses that may help the business grow.  

To travel around the city, GoFast users use a mobile app. The service can be used as follows:  
- without a subscription:  
  - no subscription fee;  
  - cost per minute of a ride — 88 rubles;  
  - start ride cost — 5050 rubles;  
- with an Ultra subscription:  
  - subscription fee — 199199 rubles per month;  
  - cost per minute of a ride — 66 rubles;  
  - start ride cost — free.  

## Data Description  
The main data includes information about users, their rides, and subscriptions (presented in three files, respectively):  

**Users — users_go.csv**  
user_id — unique user identifier  
name — user name  
age — age  
city — city  
subscription_type — subscription type (free, ultra)  

**Rides — rides_go.csv**  
user_id — unique user identifier  
distance — distance traveled by the user in the current session (in meters)  
duration — session duration (in minutes) — time from the moment the user presses the "Start Ride" button until they press the "End Ride" button  
date — date of the ride  

**Subscriptions — subscriptions_go.csv**  
subscription_type — subscription type  
minute_price — price per minute of a ride for this subscription  
start_ride_price — start ride cost  
subscription_fee — monthly subscription fee  

## Hypothesis Testing  
The product managers of the service want to increase the number of subscribed users. To do this, they plan to run various promotions, but first, they need to determine several important points.  
1. It is essential to understand whether subscribed users spend more time on rides. If so, subscribed users may be more "profitable" for the company. Test the hypothesis. Use the initial data on each session duration separately for subscribers and those without a subscription.  
2. A ride distance of 3130 meters is optimal in terms of scooter wear and tear. Can we say that the average distance traveled by subscribed users per ride does not exceed 3130 meters? Test the hypothesis and draw conclusions.  
3. Test the hypothesis that monthly revenue from subscribed users will be higher each month than from non-subscribed users. Draw a conclusion.  
4. Imagine this scenario: the service's technical team updated the servers that the mobile app interacts with. They hope that this will significantly reduce the number of support requests. A certain file contains data on the number of support requests for each user before and after the update. Which test would you need to verify this hypothesis?  

## Distributions  
1. The GoFast marketing department has been tasked with running a promotion offering promo codes for one free month of subscription, in which at least 100 existing clients should renew this subscription. That is, at the end of the subscription period, the user can either cancel it or renew it by making the corresponding payment. This promotion has been run before, and it was found that 10% of users renew the subscription after the free trial period. Determine the minimum number of promo codes to be sent out so that the probability of failing to meet the goal is approximately 5%. Select distribution parameters to describe this situation, plot the distribution, and formulate an answer regarding the number of promo codes needed.  

2. The marketing department sends push notifications to clients in the mobile app. Clients may open it or not. It is known that around 40% of recipients open the notification. The department plans to send 1 million notifications. Use approximation to plot an approximate distribution and estimate the probability that no more than 399,500 users will open the notification.  

Specific data analysis steps are provided throughout the notebook text.  

In this project, the following aspects of **Statistical Data Analysis** were covered:  
- Introduction to statistical data analysis (relationship analysis using statistical methods, statistical significance, hypotheses, and confidence intervals)  
- Combinatorics  
- Probability theory  
- Descriptive statistics  
- Random variables  
- Distributions  
- Hypothesis testing  