import json
import requests
import numpy as np
from flask import Flask, request, render_template

app = Flask(__name__)
url = ' http://student_mental_api:80/predict'
headers = {'Content-Type':'application/json'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    '''
    pour l'affichage sur html
    '''

    features = request.form.to_dict()
    inference_data = json.dumps(features)
    r = requests.post(url, data=inference_data, headers=headers)

    response_content_str = r.content.decode('utf-8')
    response_json = json.loads(response_content_str)
    return render_template('index.html', prediction_text='Student Mental health : {} '.format(response_json["prediction"]))

if __name__ == "__main__":
    app.run(debug=True)