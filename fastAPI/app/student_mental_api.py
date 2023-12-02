import uvicorn
from fastapi import FastAPI
from variables import StudentVariables
import numpy
import pickle
import pandas as pd
import onnxruntime as rt
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import QuantileTransformer

# Create app object 
app = FastAPI()

# Load model scalar
pickle_in = open("artifacts/scaler.pkl", "rb")
scaler = pickle.load(pickle_in)

# Load the model
sess = rt.InferenceSession("artifacts/lr.onnx")
input_name = sess.get_inputs()[0].name
label_name = sess.get_outputs()[0].name

# API Endpoints
@app.get('/')
def index():
    return {'Hello': 'Welcome to student mental health prediction service, access the api docs and test the API at http://0.0.0.0/docs.'}


@app.post('/predict')
def predict_weather(data: StudentVariables):
    data = data.dict()

    # fetch input data using data varaibles
    gender = data['gender']
    age = data['age']
    marital = data['marital']
    anxiety = data['anxiety']
    panic = data['panic']
    specialist = data['specialist']
    course = data['course']
    year = data['year']
    cgpa = data['cgpa']



    data_to_pred = numpy.array([[gender, age, marital, anxiety,
                                 panic, specialist, course,year,cgpa]])

    # Scale input data
    data_to_pred = scaler.fit_transform(data_to_pred.reshape(1, 9))

    # Model inference
    prediction = sess.run(
        [label_name], {input_name: data_to_pred.astype(numpy.float32)})[0]

    if(prediction[0] == 1):
        prediction = "Depression"
    else:
        prediction = "No Depression"
    return {
        'prediction': prediction
    }