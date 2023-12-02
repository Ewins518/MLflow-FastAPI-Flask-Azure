# MLflow-FastAPI-Flask-Azure-Docker

# Overview
This project's goal is to :
- use MLflow for models tracking, 
- save the best model in *ONNX* format 
- build a *REST API* for the best model using *FastAPI*
- package the API as a container using *Docker* and consume it using *Postman*
- create a dedicated application (web) to consume our API using *Flask*
- package our application as a container using *Docker*
- deploy our API using *Heroku*
- deploy our containerized API using *Azure Container Instance*
- deploy our model as a service using *Azure ML SDK* and *Mlflow*

## Run this project

1. Clone this repository to your local machine:

```bash
git clone git@github.com:Ewins518/MLflow-FastAPI-Flask-Azure.git
```

2. Navigate to the project directory:

```bash
cd MLflow-FastAPI-Flask-Azure
```

3. Open jupyter notebook and run *MLOps_assignement.ipynb*

4. Open Mlflow UI to visualize and compare models

```bash
mlflow ui -p 1234
```

![Screenshot](/screenshot/1.png)

5. Build Docker image of FastAPI app:

```bash
cd fastAPI
docker build -t fastapi .
```
6. Do the same with flask_app:

```bash
cd ../flask_app
docker build -t flask_app .
```
7. Run the docker compose inside flask_app to run the both container (FastAPI and Flask)

```bash
docker compose up -d
```
The container can be opened in the browser

![Screenshot](/screenshot/2.png)
![Screenshot](/screenshot/3.png)
![Screenshot](/screenshot/4.png)

Notice that the flask App use FastAPI app for inferences. In other word, the both containers communicated with each other .

8. Now navigate to heroku_app folder to deploy the API on Heroku.
![Screenshot](/screenshot/5.png)

You can the heroku link in the picture.

9. Deploy the containerized API using Azure Container Instance
![Screenshot](/screenshot/6.png)

Notice here also the link provide by Azure

10. Deploy the model as a service using Azure ML SDK and Mlflow

Navigate to *AzureML_SDK_Mlflow* folder and run *Deploy local and ACI.ipynb*

Don't forget to create a *Azure Machine learning* resource on Azure portal.

![Screenshot](/screenshot/7.png)
![Screenshot](/screenshot/8.png)