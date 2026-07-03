# Employee Performance Prediction using Machine Learning

## Project Overview

This project demonstrates the complete Machine Learning workflow for analyzing and predicting employee performance using a corporate employee dataset. The project includes data understanding, exploratory data analysis, feature engineering, feature selection, multiple regression models, hyperparameter tuning, model evaluation, explainable AI, and deployment preparation.

The main objective is to identify important factors affecting employee performance and build an efficient machine learning model for performance prediction.

---

## Dataset

**Dataset Name:** Corporate_AI_Employee_Dataset.csv

The dataset contains employee-related information such as:

- Employee details
- Department information
- Education level
- Experience
- Salary details
- Coding skills
- AI training hours
- Performance-related metrics

The dataset is analyzed to understand employee trends and predict performance outcomes.

---

## Technologies Used

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- XGBoost
- Joblib

---

## Project Workflow

### 1. Data Understanding

- Loaded the employee dataset
- Explored dataset features
- Identified numerical and categorical columns
- Checked memory usage
- Detected duplicate records
- Generated data quality report

---

### 2. Exploratory Data Analysis (EDA)

Performed detailed analysis including:

- Skewness detection
- Multicollinearity analysis using VIF
- Correlation analysis
- Department-wise performance visualization
- Education level impact analysis

---

### 3. Feature Engineering

Created new meaningful features:

- Experience Level  
  - Junior
  - Mid
  - Senior
  - Expert

- Salary Bands using quantiles
- Performance Index
- Coding Score and AI Training interaction feature
- One-Hot Encoding for categorical variables

---

### 4. Feature Selection

Different feature selection techniques were implemented:

- Mutual Information Regression
- Recursive Feature Elimination (RFE)
- SelectKBest with F-Regression

The best features were selected by comparing all methods.

---

## Machine Learning Models Implemented

### Regression Models

- Linear Regression
- Ridge Regression
- Lasso Regression
- ElasticNet Regression

### Tree-Based Models

- Decision Tree Regressor
- Random Forest Regressor
- Extra Trees Regressor
- Gradient Boosting Regressor
- XGBoost Regressor

---

## Model Evaluation Metrics

Models were evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score
- Adjusted R² Score
- 10-Fold Cross Validation

---

## Hyperparameter Optimization

Performed model tuning using:

### GridSearchCV
Used for Random Forest optimization.

### RandomizedSearchCV
Used for XGBoost optimization.

Tuned models were compared with baseline models.

---

## Explainable AI

Feature importance analysis was performed to understand the factors influencing employee performance prediction.

Top contributing features were identified to provide business insights.

---

## Model Deployment Approach

A complete Machine Learning pipeline was created including:

- Data preprocessing
- Feature engineering
- Feature selection
- Model training
- Model evaluation
- Model serialization

The trained model was saved using:
