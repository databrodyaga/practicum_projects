# Borrower Reliability Research

## Project Description
The client is the bank's credit department.   
**We need to understand** whether a client's marital status and number of children affect the likelihood of repaying the loan on time.   
The bank provided input data — statistics on clients' solvency.  
The research results will be taken into account when building a credit scoring model — a special system that assesses a potential borrower's ability to repay the loan to the bank.

## Data Description
- children — number of children in the family
- days_employed — total work experience in days
- dob_years — client's age in years
- education — client's education level
- education_id — education level identifier
- family_status — marital status
- family_status_id — marital status identifier
- gender — client's gender
- income_type — type of employment
- debt — whether there was a debt on loan repayment
- total_income — monthly income
- purpose — purpose of obtaining the loan

The specific data analysis steps are provided throughout the notebook.  

At the end of the analysis, we need to answer the following questions:  
- Is there a relationship between the number of children and loan repayment on time?  
- Is there a relationship between marital status and loan repayment on time?  
- Is there a relationship between income level and loan repayment on time?  
- How do different loan purposes affect its repayment on time?  
- Provide possible reasons for missing data in the original dataset.  
- Explain why filling in missing values with the median is the best solution for quantitative variables.  

This project covers the following aspects of **Data Preprocessing**:  
- Introduction to data preprocessing (cleaning data from outliers, missing values, and duplicates)  
- Changing data types  
- Duplicate search  
- Data categorization  
- Systematic and critical thinking in an analyst's work