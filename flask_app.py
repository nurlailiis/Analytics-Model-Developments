
# A very simple Flask Hello World app for you to get started with...

#from flask import Flask
from flask import Flask, request, jsonify
import numpy as np
from sklearn.externals import joblib

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

model = joblib.load(open('/home/nurlailiis/mysite/model_DT.pkl','rb'))
#pickle.load(open('model_DT.pkl','rb'))

@app.route('/api',methods=['POST'])
def predict():
    # Get the data from the POST request.
    datas = request.get_json(force=True)

    pred = []
    for data in datas:
        # Make prediction using model loaded from disk as per the data.
        # exp : experience(fitur input)
        prediction = model.predict([np.array([data['EDUCATION'],data['AGE'],data['PAY_1'],data['PAY_2'],data['PAY_3']])])
    #     features = [np.array([2,45,1,0,0])]
    #     prediction = model.predict(features)

        # Take the first value of prediction
        output = int(prediction[0])
        out = 'In the next month he/she payment wil be late' if output==1 else 'In the next month he/she payment wil not be late'
        pred.append(out)
    return jsonify(pred)


