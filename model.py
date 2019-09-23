
# coding: utf-8

# In[ ]:



# coding: utf-8

# In[ ]:


# Simple Linear Regression

'''
This model predicts the salary of the employ based on experience using simple linear regression model.
'''

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import requests
import json

# Importing the dataset
dataset = pd.read_csv('training.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
# test size: 30%
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# Fitting Simple Linear Regression to the Training set
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
decisiontree = DecisionTreeClassifier()
decisiontree.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

# Saving model to disk
pickle.dump(regressor, open('model_DT.pkl','wb'))

