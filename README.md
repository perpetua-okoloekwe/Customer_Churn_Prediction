Customer Churn Prediction Using Machine Learning
 Project Overview
Customer churn is a major challenge for telecom companies because losing customers directly impacts revenue and business growth.
The goal of this project is to identify factors associated with customer churn and build machine learning models capable of predicting customers who are likely to leave.
Using the IBM Telco Customer Churn dataset, I performed exploratory data analysis, investigated missing values, removed data leakage, engineered features, and compared multiple machine learning models to determine the most effective approach for churn prediction.

 Business Problem
Telecommunication companies invest significant resources in acquiring customers.
When customers leave, companies lose:

Revenue
Customer lifetime value
Marketing and acquisition investments

The ability to identify customers at risk of churning allows businesses to proactively implement retention strategies and improve customer satisfaction.

 Dataset Information
Dataset: IBM Telco Customer Churn Dataset
Dataset Characteristics

7,043 customer records
50 initial features
Binary classification problem
Target Variable: ChurnLabel

Target Distribution

















ClassCountNo Churn5,174Churn1,869
The dataset exhibits moderate class imbalance, making evaluation metrics such as Precision, Recall, F1 Score, and ROC-AUC particularly important.

 Exploratory Data Analysis (EDA)
The dataset was explored to understand:

Data types
Missing values
Class balance
Feature relationships
Potential data leakage

Key Findings
Satisfaction Score
Customers who churned had significantly lower satisfaction scores than customers who stayed.
Offers
Churn rates varied considerably across offer categories, suggesting promotional offers play an important role in customer retention.
Missing Values
Not all missing values represented missing data.
Examples:

Missing InternetType corresponded to customers without internet service.
Missing Offer values were interpreted as customers who did not receive an offer.


 Data Cleaning & Preparation
Removed Features
The following columns were removed:

CustomerID
Country
State
Quarter
ChurnReason
ChurnCategory
CustomerStatus
ChurnScore
City
ZipCode
Latitude
Longitude

Reason for Removal
These columns represented:

Identifiers
Data leakage
Non-informative features
High-cardinality variables introducing noise

Additional Preparation

Missing values handled
Target variable encoded
Categorical variables one-hot encoded
Stratified train-test split applied
Numerical features standardized for Logistic Regression


 Models Trained
1. Logistic Regression
Performance





























MetricScoreAccuracy96.17%Precision95%Recall90%F1 Score93%ROC-AUC0.992

2. Random Forest
Performance





























MetricScoreAccuracy95.53%Precision97%Recall86%F1 Score91%ROC-AUC0.984

 Model Comparison



































MetricLogistic RegressionRandom ForestAccuracy96.17%95.53%Precision95%97%Recall90%86%F1 Score93%91%ROC-AUC0.9920.984
Best Model
Despite being the simpler algorithm, Logistic Regression outperformed Random Forest in Recall and ROC-AUC, making it more suitable for identifying customers at risk of churn.

 Key Business Insights
Factors Associated With Lower Churn

Higher Satisfaction Scores
More Customer Referrals
Longer Customer Tenure
Online Security Services
Premium Technical Support
One-Year and Two-Year Contracts

Factors Associated With Higher Churn

Higher Monthly Charges
Certain Offer Categories
Specific customer behavioral patterns


 Key Lesson Learned
One of the most important lessons from this project is:

Machine learning performance starts long before model training.

The strongest contributor to performance was not model complexity but:

Understanding the data
Investigating missing values
Removing data leakage
Selecting meaningful features
Preserving business context

This project reinforced how effective data preparation can allow a simple model to outperform a more complex one.

 Technologies Used

Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Jupyter Notebook / Google Colab


 Future Improvements
Potential future enhancements include:

Hyperparameter tuning
Gradient Boosting (XGBoost, LightGBM)
Neural Network implementation
Deployment using Streamlit or Flask
Automated customer churn prediction dashboard


 Author
Perpetua Okoloekwe
AI Engineering Journey – Project 2
Learning in public, one project at a time 
