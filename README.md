# HousingGuru
This project demonstrates a simple machine learning pipeline for predicting house prices using the California Housing dataset. The project trains a linear regression model and deploys it using a FastAPI web application. It includes features for training, saving, and serving the model as an API to make predictions.

## Features:
- **Model Training:** Trains a Linear Regression model using Scikit-learn.
- **Model Saving/Loading:** Saves the trained model as a pickle file (`model.pkl`) for future use.
- **API Deployment:** Deploys the model using FastAPI, enabling predictions through a web interface.

## Technologies Used:
- Python
- Scikit-learn
- FastAPI
- Uvicorn (for running the API)

## Purpose:
This project was created as part of a portfolio to demonstrate building and deploying a machine learning model into production, as required for real-world machine learning projects.

## How to Use:
1. Clone the repository.
2. Train the model (or use the pre-saved `model.pkl` file).
3. Run the FastAPI application to serve predictions via an API.
