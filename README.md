#  Customer Churn Prediction Using Machine Learning

##  Project Overview

This project aims to predict customer churn in a telecom company using machine learning.

Using the IBM Telco Customer Churn dataset, I explored customer behavior, investigated missing values, removed data leakage, engineered features, and trained machine learning models to identify customers likely to leave.

Two models were evaluated:

- Logistic Regression
- Random Forest

Logistic Regression achieved the best overall performance with:

- Accuracy: 96.17%
- Precision: 95%
- Recall: 90%
- ROC-AUC: 0.992

The project demonstrates how careful data preparation and feature selection can significantly impact machine learning performance.
---

##  Project Structure

```text
Customer-Churn-Prediction/
│
├── README.md
│
├── images/
│   ├── Churn Distribution.png
│   ├── Missing Values.png
│   ├── Satisfaction Score vs Churn.png
│   ├── Contract vs Churn.png
│   ├── Logistic Regression Confusion Matrix.png
│   ├── Model Comparison.png
│   └── Top Predictors.png
│
└── notebooks/
    └── Customer_Churn_Prediction.ipynb
```

##  Business Problem

Telecommunication companies invest significant resources in acquiring customers.

When customers leave, companies lose:

- Revenue
- Customer Lifetime Value (CLTV)
- Marketing and acquisition investments

The ability to identify customers at risk of churning allows businesses to proactively implement retention strategies and improve customer satisfaction.

---

##  Dataset Information

**Dataset:** IBM Telco Customer Churn Dataset

### Dataset Characteristics

- 7,043 customer records
- 50 original features
- Binary classification problem
- Target Variable: `ChurnLabel`

### Target Distribution

| Class | Count |
|---------|---------:|
| No Churn | 5,174 |
| Churn | 1,869 |

The dataset exhibits moderate class imbalance, making evaluation metrics such as Precision, Recall, F1 Score, and ROC-AUC particularly important.

---

##  Quick Results

### Best Model: Logistic Regression

| Metric | Score |
|---------|---------:|
| Accuracy | 96.17% |
| Precision | 95% |
| Recall | 90% |
| F1 Score | 93% |
| ROC-AUC | 0.992 |

### Key Takeaways

- Logistic Regression outperformed Random Forest

- Customer Satisfaction was the strongest predictor of churn

- Longer contracts were associated with lower churn

- Higher monthly charges were associated with increased churn risk

- Careful data preparation contributed significantly to model performance
  
---

## 📊 Project Visualizations

### Churn Distribution

images/Churn_Distribution.png

### Model Comparison

images/Model_Comparison.png

### Top Predictors of Churn

images/Top_Predictors.png

---

##  Exploratory Data Analysis (EDA)

The dataset was explored to understand:

- Data types
- Missing values
- Class balance
- Feature relationships
- Potential data leakage

### Key Findings

#### Satisfaction Score

Customers who churned had significantly lower satisfaction scores than customers who stayed.

#### Offer Types

Churn rates varied considerably across offer categories, suggesting promotional offers play an important role in customer retention.

#### Missing Values

Not all missing values represented missing data.

Examples:

- Missing `InternetType` corresponded to customers without internet service.
- Missing `Offer` values were interpreted as customers who did not receive an offer.

---

##  Data Cleaning & Preparation

### Removed Features

The following columns were removed:

- CustomerID
- Country
- State
- Quarter
- ChurnReason
- ChurnCategory
- CustomerStatus
- ChurnScore
- City
- ZipCode
- Latitude
- Longitude

### Reason for Removal

These columns represented:

- Identifiers
- Data leakage
- Non-informative variables
- High-cardinality variables introducing noise

### Additional Preparation

- Missing values handled
- Target variable encoded
- Categorical variables one-hot encoded
- Stratified train-test split applied
- Numerical features standardized for Logistic Regression

---

##  Models Trained

### 1️⃣ Logistic Regression

#### Performance

| Metric | Score |
|---------|---------:|
| Accuracy | 96.17% |
| Precision | 95% |
| Recall | 90% |
| F1 Score | 93% |
| ROC-AUC | 0.992 |

---

### 2️⃣ Random Forest

#### Performance

| Metric | Score |
|---------|---------:|
| Accuracy | 95.53% |
| Precision | 97% |
| Recall | 86% |
| F1 Score | 91% |
| ROC-AUC | 0.984 |

---

##  Model Comparison

| Metric | Logistic Regression | Random Forest |
|---------|---------:|---------:|
| Accuracy | 96.17% | 95.53% |
| Precision | 95% | 97% |
| Recall | 90% | 86% |
| F1 Score | 93% | 91% |
| ROC-AUC | 0.992 | 0.984 |

###  Best Model

Despite being the simpler algorithm, **Logistic Regression outperformed Random Forest in Recall and ROC-AUC**, making it the preferred model for identifying customers at risk of churn.

---

##  Key Business Insights

### Factors Associated with Lower Churn

- Higher Satisfaction Scores
- More Customer Referrals
- Longer Customer Tenure
- Online Security Services
- Premium Technical Support
- One-Year and Two-Year Contracts

### Factors Associated with Higher Churn

- Higher Monthly Charges
- Certain Offer Categories
- Specific customer behavioral characteristics

---

##  Key Lesson Learned

One of the most valuable lessons from this project was:

> **Machine learning performance starts long before model training.**

The strongest contributor to performance was not model complexity but:

- Understanding the data
- Investigating missing values
- Removing data leakage
- Selecting meaningful features
- Preserving business context

This project reinforced how effective data preparation can allow a simple model to outperform a more complex one.

---

## Business Recommendations

Based on the findings from this analysis, the following actions are recommended:

1. Improve customer satisfaction through proactive engagement and support initiatives.

2. Encourage adoption of longer-term contracts through incentives and loyalty programs.

3. Promote Online Security and Premium Tech Support services as retention tools.

4. Identify high monthly charge customers for targeted retention campaigns.

5. Expand referral programs to increase customer engagement and loyalty.

---

##  Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Google Colab

---

##  Future Improvements

Potential future enhancements include:

- Hyperparameter tuning
- Gradient Boosting (XGBoost, LightGBM)
- Neural Network implementation
- Streamlit deployment
- Interactive churn prediction dashboard

---

##  Author

**Perpetua Okoloekwe**

AI Engineering Journey — Project 2

Learning in public, one project at a time 

---
