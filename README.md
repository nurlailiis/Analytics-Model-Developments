# Analytics-Model-Development
## Introduction
In this section we try to solve the problem of creditor using python by Credit Scoring. In pursuit to increase their market share, banks often issue credit cards to ineligible customer without adequate background checks. Also, many customers used their credit card beyond their repayment capabilities leading to high debt accumulation. Identifying the risky and non-risky customers is the biggest challenge for banks. So, the problem we are trying to analyze is how to identify the risky andnon-risky customers, helping the bank to decide if a **customer has the potential to late or has not late pay their credit in the next month.** <br>
We solve the problem using Simple Data Flow Python Environment.
![Analytics-Model-Development](https://raw.githubusercontent.com/nurlailiis/Analytics-Model-Developments/master/image/Simple%20Data%20Flow.PNG)
Based on above image, we know that Simple Data Flow Python Environment consist of:   
  * **User Space**: environment that can view by user/client (for example **Front end** websites bots). In this section, we practiced using Postman
  * **Server Space**: server as a provider and environment that API's work (consist of: python flask and Machine Learning model). In this section, we practiced Machine Learning model extension pickel (.pkl) 
---
## Get Started
The variables used to calculate credit scoring are:
  * PAY_AMT1: Number of credit payments made by customers in the first month.
  * PAY_AMT2: Number of credit payments made by customers in the second month.
  * PAY_AMT3: Number of credit payments made by customers in the third month. 
  <br>
---
<br>
## Hands On
We try to solve that problem using **Decision Three algorithm** to predict whether a customer will be late paying credit in the fourth month. 
The resulting output is 2, namely:
  * 0: Customers are predicted not to be late in making credit payments.
  * 1: Customers are predicted to be late in making credit payments.
