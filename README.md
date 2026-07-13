#  Cal_X_AI - AI Powered Calorie Prediction System

##  Overview

Cal_X_AI is a Machine Learning-powered web application that predicts a user's daily calorie requirements based on personal and lifestyle information. The application combines a trained regression model with a Django web interface to provide personalized calorie recommendations for different fitness goals such as weight loss, weight maintenance, and muscle gain.

The project demonstrates the complete Machine Learning workflow—from data preprocessing and feature engineering to model training, evaluation, serialization, and deployment using Django.

---

#  Features

* Predicts daily calorie requirements
* User-friendly web interface built with Django
* Real-time predictions
* Automatic feature engineering from user inputs
* Supports multiple activity levels
* Supports multiple fitness goals
* Trained Machine Learning model
* Fast predictions using saved model files
* Responsive web interface

---

#  Tech Stack

### Programming Language

* Python 3.x

### Backend

* Django 6

### Machine Learning

* Scikit-learn

### Data Analysis

* Pandas
* NumPy

### Data Visualization

* Matplotlib

### Model Serialization

* Joblib

### Database

* SQLite3

### Frontend

* HTML5
* CSS3
* JavaScript
* Django Templates

---

#  Python Libraries Used

```text
Django
pandas
numpy
scikit-learn
matplotlib
joblib
scipy
sqlite3
```

Major Python modules used:

```python
pandas
numpy
matplotlib.pyplot

sklearn.model_selection
sklearn.linear_model
sklearn.preprocessing
sklearn.metrics

joblib
scipy.stats
```

---

#  Machine Learning Techniques Used

## Data Cleaning

* Handling missing values
* Removing unnecessary columns
* Data type conversion
* Feature selection

---

## Feature Engineering

Additional features were generated from the user's input to improve prediction accuracy.

Examples include:

* BMI
* Body Fat Percentage
* Lean Body Mass
* Basal Metabolic Rate (BMR)
* Total Daily Energy Expenditure (TDEE)
* Weight to Height Ratio
* Fat Free Mass Index
* Activity Multiplier
* Daily Energy Expenditure per Kg
* Gender-Weight Interaction
* Gender-Height Interaction
* Calorie Adjustment Direction

---

## Encoding

Categorical variables were encoded using Label Encoding.

Encoded features include:

* Gender
* Activity Level
* Fitness Goal

The encoders were saved using Joblib and reused during prediction.

---

## Feature Scaling

Numerical features were standardized before training using:

* StandardScaler

The fitted scaler was also saved with Joblib for deployment.

---

## Model Training

The dataset was divided using:

* Train-Test Split

Regression model used:

* Linear Regression

---

## Model Evaluation

Performance was evaluated using:

* R² Score

---

## Deployment

The trained model and preprocessing objects were serialized using Joblib.

Saved files include:

* Trained ML Model
* StandardScaler
* Gender Encoder
* Activity Level Encoder
* Purpose Encoder

These files are loaded by Django during prediction.

---

#  Project Workflow

```
Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Encoding
      │
      ▼
Feature Scaling
      │
      ▼
Train-Test Split
      │
      ▼
Linear Regression Model
      │
      ▼
Model Evaluation
      │
      ▼
Save Model (Joblib)
      │
      ▼
Django Integration
      │
      ▼
User Prediction
```

---

# 📊 Input Parameters

The model accepts the following user inputs:

* Age
* Gender
* Height
* Weight
* Activity Level
* Fitness Goal

These inputs are transformed into engineered features before prediction.

---

#  Output

The application predicts:

* Estimated Daily Calorie Requirement (Calories/Day)

---

#  Future Improvements

* Support multiple ML algorithms
* Compare model performance
* User authentication
* Save prediction history
* Diet recommendations
* Workout recommendations
* BMI dashboard
* Graphical analytics
* REST API
* Docker deployment
* Cloud deployment (AWS/Azure/GCP)

---

#  Project Structure

```
Cal_X_AI/
│
├── predictor/
├── templates/
├── static/
├── models/
│
├── calorie_model.joblib
├── scaler.joblib
├── gender_encoder.joblib
├── activity_encoder.joblib
├── purpose_encoder.joblib
│
├── db.sqlite3
├── manage.py
└── README.md
```

---

#  Author

**Devansh Chandel**

MCA Student | Data Science & Machine Learning Enthusiast

---

#  License

This project is intended for educational and learning purposes. Feel free to fork, modify, and improve it.

