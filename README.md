# 📊 Telecom Customer Churn Analysis & Prediction  

## ✅ Overview  
Customer churn is a critical challenge for telecom companies. Retaining existing customers is more cost-effective than acquiring new ones. This project uses  **data analysis**, **machine learning (XGBoost with SMOTE)**, and **Power BI dashboards** to identify customers likely to churn and empower decision-makers with data-driven insights.

---

## ✅ Project Objectives

- Analyze key factors influencing telecom customer churn
- Build a robust and interpretable churn prediction model
- Predict churn risk for new customers
- Visualize results using interactive dashboards

---

## 🧠 Tech Stack

| Category        | Tools/Technologies                          |
|----------------|----------------------------------------------|
| **Language**    | Python                                      |
| **ML Libraries**| pandas, numpy, scikit-learn, XGBoost, imbalanced-learn |
| **Visualization** | matplotlib, seaborn, Power BI             |
| **Output**      | CSV (predicted churners), Power BI Dashboards |

---

## 📁 Dataset Overview

- **File**: `prediction_data.xlsx`
- **Sheets**:
  - `vw_churndata`: Historical customer data for model training
  - `vw_joindata`: New customer data for prediction
- **Target Variable**: `Customer_Status`  
  (Mapped as: `Stayed` = 0, `Churned` = 1)

---

## 🔧 Methodology

### 1. 📌 Data Preprocessing
- Dropped unnecessary columns: `Customer_ID`, `Churn_Category`, `Churn_Reason`
- Applied **Label Encoding** to categorical columns
- Filtered out any irrelevant status values
- Mapped target variable (`Customer_Status`) to 0 and 1

### 2. ⚖️ Class Imbalance Handling
- Used **SMOTE** (Synthetic Minority Over-sampling Technique) to balance training data

### 3. 🚀 Model Building with XGBoost
- Algorithm: **XGBoost Classifier**
- Parameters:
  - `n_estimators=300`
  - `learning_rate=0.1`
  - `max_depth=6`
  - `scale_pos_weight` to address imbalance
- Custom decision threshold: **0.4** to improve recall for churn prediction

### 4. 📉 Model Evaluation

| Metric          | Class 0 (Stayed) | Class 1 (Churned) | Overall |
|-----------------|------------------|-------------------|---------|
| Precision       | 0.90             | 0.65              |         |
| Recall          | 0.83             | 0.78              |         |
| F1-Score        | 0.86             | 0.71              |         |
| **Accuracy**    |                  |                   | **82%** |
| **ROC-AUC**     |                  |                   | **0.885** |
| **Test Size**   | 855              | 347               | 1202    

- ✅ High **recall** on churners helps reduce missed high-risk customers
- ✅ ROC-AUC of **0.885** indicates strong classifier separation
- ✅ Balanced F1-scores reflect reliable overall model behavior

---

### 5. 🔍 Churn Prediction on New Customers
- Used sheet `vw_joindata`
- Encoded categorical variables using saved encoders
- Applied trained model to predict churn risk
- Filtered predicted churners and saved output

📁 **Output File**: `prediction_results.csv`

---

## 📊 Dashboards (Power BI)

### 🔹 Churn Summary Dashboard

Displays:
- 📈 Total Customers, Churned Customers, Churn Rate
- 📊 Churn distribution by Gender, Age Group, State
- 🔍 Contract Type, Internet Type, Payment Method
- 🧾 Services Impacting Churn (e.g., Streaming, Backup)

**Preview:**  
![Churn Summary](https://github.com/manasa-dumpala2003/Telecom-churn-analysis/blob/main/Telecom%20churn%20analysis.png)  

---
### 🔹 Churn Prediction Dashboard

Displays:
- 🔺 Predicted high-risk customers
- 📍 Distribution by State, Contract, Tenure
- 🧮 Monthly Charges, Refund Amounts, Total Revenue
- 📋 Detailed customer list with churn risk labels


**Preview:**  
![Churn Prediction](https://github.com/manasa-dumpala2003/Telecom-churn-analysis/blob/main/ChurnPrediction.png)  

---

📌 Helps business stakeholders **act quickly on churn threats**



**Future Enhancement:**
- Deploy real-time prediction API.
- Automate Power BI dashboard refresh.

