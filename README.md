# Analytics-Model-Development
## Introduction
In this section we try to solve the problem of creditor using python by Credit Scoring. In pursuit to increase their market share, banks often issue credit cards to ineligible customer without adequate background checks. Also, many customers used their credit card beyond their repayment capabilities leading to high debt accumulation. Identifying the risky and non-risky customers is the biggest challenge for banks. So, the problem we are trying to analyze is how to identify the risky and non-risky customers, helping the bank to decide if a **customer has the potential to late or has not late pay their credit in the next month.** <br>
We solve the problem using Simple Data Flow Python Environment.
![Analytics-Model-Development](https://raw.githubusercontent.com/nurlailiis/Analytics-Model-Developments/master/image/Simple%20Data%20Flow.PNG)<br>
Based on above image, we know that Simple Data Flow Python Environment consist of:   
  * **User Space**: environment that can view by user/client (for example **Front end** websites bots). In this section, we practiced using Postman
  * **Server Space**: server as a provider and environment that API's work (consist of: python flask and Machine Learning model). In this section, we practiced Machine Learning model extension pickel (.pkl) 
---
## Get Started
The variables used to calculate credit scoring are:
  * PAY_AMT1: Number of credit payments made by customers in the first month.
  * PAY_AMT2: Number of credit payments made by customers in the second month.
  * PAY_AMT3: Number of credit payments made by customers in the third month. 
---
## Hands On
We try to solve that problem using **Decision Three algorithm** to predict whether a customer will be late paying credit in the fourth month. 
The resulting output is 2, namely:
  * 0: Customers are predicted not to be late in making credit payments.
  * 1: Customers are predicted to be late in making credit payments.
### 1. Build Python Environment<br>
You can [pythonanywhere](https://pythonanywhere.com) to build server for load model that you have made. You should upload two main files, consist of:
 * flask_app.py: file as a "server" that stored in pythonanywhere with the request API. You can see the content of flask_app.py that we made at: https://www.pythonanywhere.com/user/nurlailiis/shares/1b910ec220234258aff93da4d9357533/
 * model_DT.pkl: file that contain model of Decision Tree for Credit Scoring to do analytics model development.
 *Additional Information:
 * request.py: file that contain url and value that you want to test
 * training.csv: file csv that contain the data to build this model
### 2. Build Model With Postman<br>
  1. **Install Postman**<br>
  You can use Postman Sofware and download to Windows Version in [Link](https://www.getpostman.com/downloads/) or using the extension from Google Chrome for alternative.<br>
  2. **Run Postman**<br>
  After you successful install postman, you can open it from windows or alternative solution from Google Chrome extension. Then follow the instruction to close the pop up.
  ![image](https://raw.githubusercontent.com/nurlailiis/Analytics-Model-Developments/master/image/Postman%201.PNG)
  3. **Builder the Postman**<br>
  You should change the type become **"POST" in red mark** based on method to test the API, the fill the **blue mark with your url request API** with this url nurlailiis.pythonanywhere.com/api, choose **Body in green mark**, choose the Beautify **raw and select JSON in the yellow mark**. <br>
  ![image1](https://raw.githubusercontent.com/nurlailiis/Analytics-Model-Developments/master/image/Postman%202.PNG)
  After that you should input the text become JSON on the Body of Postman as follows:
  * **Input 1 data**<br>
  [
     {"EDUCATION":1,"AGE":25,"PAY_1":1,"PAY_2":1,"PAY_3":1}
  ]
  * **Input more than 1 data (for example 10 data or you can check on request.py for the dataset**<br>
  [
     {"EDUCATION":1,"AGE":25,"PAY_1":1,"PAY_2":1,"PAY_3":1},
     {"EDUCATION":2,"AGE":40,"PAY_1":2,"PAY_2":2,"PAY_3":2},
     {"EDUCATION":3,"AGE":35,"PAY_1":1,"PAY_2":0,"PAY_3":1},
     {"EDUCATION":0,"AGE":20,"PAY_1":0,"PAY_2":1,"PAY_3":2},
     {"EDUCATION":1,"AGE":25,"PAY_1":1,"PAY_2":2,"PAY_3":0},
     {"EDUCATION":2,"AGE":20,"PAY_1":2,"PAY_2":0,"PAY_3":1},
     {"EDUCATION":3,"AGE":44,"PAY_1":0,"PAY_2":1,"PAY_3":2},
     {"EDUCATION":1,"AGE":30,"PAY_1":1,"PAY_2":2,"PAY_3":0},
     {"EDUCATION":4,"AGE":21,"PAY_1":2,"PAY_2":1,"PAY_3":1},
     {"EDUCATION":1,"AGE":25,"PAY_1":1,"PAY_2":2,"PAY_3":2}
   ]<br>
   **Notes:** the data above based on the field that you choose when you build the train data on the model.<br>
   Then click button **Send** in the red mark, and **make sure you are connected to the internet** because of the url is online. Meanwhile, if you want to access when you are offline, you can use localhost.
   4. **Output Postman**<br>
   After you click button send you can see the result of Credit Scoring as follows:
   ![image3](https://raw.githubusercontent.com/nurlailiis/Analytics-Model-Developments/master/image/Postman%203.PNG)
---
## Conclusion
Based on this section we can conclude that **Web Service can build from different function, communicate the protocol, or tools to create the software**. This model use server in pythonanywhere as a server to communicate the Machine Learning model (model_DT.pkl) to user space using Postman. This model using field Education (1 = graduate school; 2 = university; 3 = high school; 4 = others), Age, and Payment from first until third month to **predict the customer will be late or not be late to pay their credit for the fourth month**. So that, based on this **web service banks can easily know how to identify the risky and non-risky customers.**
