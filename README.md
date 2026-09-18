# Student G3 Prediction

## Project Overview

This project uses Machine Learning to predict a student's final grade (G3) based on academic, demographic, social, and other student-related features.

## Objective

The main objective of this project is to build a regression model that can predict students' final grades and analyze which features have the greatest influence on the model's predictions.

## Dataset

- Dataset: Student Performance Dataset
- Total Records: 395
- Original Features: 32 input features
- Target Variable: G3 (Final Grade)
- Encoded Features: 41

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Joblib
- Google Colab

## Machine Learning Workflow

1. Data Loading
2. Data Understanding and EDA
3. Feature and Target Separation
4. Categorical Feature Encoding
5. Train-Test Split
6. Linear Regression
7. Random Forest Regression
8. Model Evaluation
9. Feature Importance Analysis
10. 5-Fold Cross Validation
11. Sample Prediction
12. Model Saving

## Models Used

### Linear Regression

Used as a baseline regression model.

### Random Forest Regressor

Used as the main prediction model with 200 decision trees.

## Model Performance

The Random Forest model achieved the following results on the test set:

- MAE: 1.173
- RMSE: 1.967
- R² Score: 0.811

### 5-Fold Cross Validation

- Mean R² Score: 0.837
- Standard Deviation: 0.033

## Feature Importance

The top features identified by the Random Forest model were:

1. G2
2. Absences
3. Reason (Home)
4. Age
5. G1

Feature importance indicates how much the model relied on a feature for its predictions; it does not by itself establish a causal relationship.

## Project Files

- `Student_grade_Prediction.ipynb` — Complete Google Colab notebook
- `student_data.csv` — Dataset
- `student_grade_model.pkl` — Trained Random Forest model
- `student_grade_features.pkl` — Encoded feature information

## Conclusion

The Random Forest Regressor provided stronger predictive performance than the Linear Regression baseline for this dataset. The project demonstrates how Machine Learning can be used to analyze student performance and predict final academic grades.

## Author

Kinjal Soni
