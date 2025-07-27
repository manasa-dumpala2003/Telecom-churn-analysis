# 📊 Telecom Customer Churn Analysis & Prediction  

## ✅ Overview  
Customer churn is a critical challenge for telecom companies. Retaining existing customers is more cost-effective than acquiring new ones. This project uses **data analysis**, **machine learning prediction**, and **Power BI dashboards** to identify customers at risk of churning and provide actionable insights.  

---

## ✅ Objectives  
- Analyze key factors influencing customer churn.  
- Build a predictive model to classify high-risk customers.  
- Create interactive dashboards for decision-making.  

---

## ✅ Tech Stack  
- **Languages:** Python  
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Joblib  
- **Visualization:** Power BI  
  
---

## ✅ Dataset  
- **File:** `prediction_data.xlsx`  
- **Sheets:**  
  - `vw_churndata`: Historical churn data for model training.  
  - `vw_joindata`: New customer data for churn prediction.  
- **Target Variable:** `Customer_Status` (`Stayed` = 0, `Churned` = 1)  

---

## ✅ Methodology  
### **1. Data Preprocessing**  
- Removed unnecessary columns: `Customer_ID`, `Churn_Category`, `Churn_Reason`.  
- Handled categorical variables using **Label Encoding**.  
- Encoded target column (`Stayed` → 0, `Churned` → 1).  

### **2. Model Building**  
- Algorithm: **Random Forest Classifier** (`n_estimators=100`).  
- Train-Test Split: **80/20**.  

### **3. Evaluation Metrics**  
- **Confusion Matrix**  
- **Classification Report**: Precision, Recall, F1-score  
- **Feature Importance Plot**  

### **4. Prediction for New Data**  
- Encoded new customer data using the same encoders.  
- Predicted churn risk.  
- Filtered customers predicted as **Churned** and saved to `prediction.csv`.  

---

## ✅ Dashboards  

### **1. Churn Summary Dashboard**  
Displays:  
✔ Total Customers & Churn Rate  
✔ Churn Rate by Gender, Age Group, Tenure  
✔ Churn by Payment Method & Contract Type  
✔ Services Impacting Churn (Internet Type, Streaming, Security)  

**Preview:**  
![Churn Summary](https://github.com/manasa-dumpala2003/Telecom-churn-analysis/blob/main/Telecom%20churn%20analysis.png)  

---

### **2. Churn Prediction Dashboard**  
Displays:  
✔ Predicted Customers at Risk (count)  
✔ Distribution by Gender, State, Age, Tenure  
✔ Contract Type & Payment Method for high-risk customers  
✔ Detailed customer list with monthly charges, revenue, refunds  

**Preview:**  
![Churn Prediction](https://github.com/manasa-dumpala2003/Telecom-churn-analysis/blob/main/ChurnPrediction.png)  

---

**Model Performance**  
Metric	Score
- Accuracy	84%
- Precision	81%
- Recall	79%
- F1-score	80%

**Future Enhancement:**
- Deploy real-time prediction API.
- Automate Power BI dashboard refresh.
- Use advanced ML models like XGBoost and CatBoost.
