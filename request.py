
# coding: utf-8

# In[ ]:


import requests

# URL
url = 'nurlailiis.pythonanywhere.com/api'

# Change the value of experience that you want to test
r = requests.post(url,json=[
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
                                ])
print(r.json())

