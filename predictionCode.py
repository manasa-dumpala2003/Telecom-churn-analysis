# ✅ Import Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import SMOTE
from xgboost import XGBClassifier

# ✅ Load Data
file_path = r"C:\Users\Admin\prediction_data.xlsx"
data = pd.read_excel(file_path, sheet_name=1)  # Training data sheet

# ✅ Drop unnecessary columns
data = data.drop(['Customer_ID', 'Churn_Category', 'Churn_Reason'], axis=1)

# ✅ Encode categorical features
columns_to_encode = [
    'Gender', 'Married', 'State', 'Value_Deal', 'Phone_Service', 'Multiple_Lines',
    'Internet_Service', 'Internet_Type', 'Online_Security', 'Online_Backup',
    'Device_Protection_Plan', 'Premium_Support', 'Streaming_TV', 'Streaming_Movies',
    'Streaming_Music', 'Unlimited_Data', 'Contract', 'Paperless_Billing',
    'Payment_Method'
]

label_encoders = {}
for column in columns_to_encode:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    label_encoders[column] = le

# ✅ Handle target variable
# Keep only rows with 'Stayed' or 'Churned'
data = data[data['Customer_Status'].isin(['Stayed', 'Churned'])]
data['Customer_Status'] = data['Customer_Status'].map({'Stayed': 0, 'Churned': 1})

# ✅ Split data into features and target
X = data.drop('Customer_Status', axis=1)
y = data['Customer_Status']

# ✅ Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ✅ Handle Class Imbalance using SMOTE
sm = SMOTE(random_state=42)
X_res, y_res = sm.fit_resample(X_train, y_train)

print(f"Before SMOTE: {y_train.value_counts()}")
print(f"After SMOTE: {y_res.value_counts()}")

# ✅ Train XGBoost Model
xgb_model = XGBClassifier(
    n_estimators=300,
    learning_rate=0.1,
    max_depth=6,
    scale_pos_weight=len(y_train[y_train==0]) / len(y_train[y_train==1]),  # handles imbalance
    eval_metric='logloss',
    random_state=42
)

xgb_model.fit(X_res, y_res)

# ✅ Predict with threshold tuning
y_prob = xgb_model.predict_proba(X_test)[:, 1]
threshold = 0.4  # Lower threshold for higher recall
y_pred = (y_prob >= threshold).astype(int)

# ✅ Evaluation
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nROC-AUC Score:", roc_auc_score(y_test, y_prob))

# ✅ Feature Importance Visualization
importances = xgb_model.feature_importances_
indices = np.argsort(importances)[::-1]

plt.figure(figsize=(15, 6))
sns.barplot(x=importances[indices], y=X.columns[indices])
plt.title('XGBoost Feature Importances')
plt.xlabel('Relative Importance')
plt.ylabel('Feature Names')
plt.show()

# ✅ Predict for New Data (Joiner Data)
new_data = pd.read_excel(file_path, sheet_name=0)  # New customer sheet

# Keep original for saving results
original_data = new_data.copy()

# Drop unused columns for prediction
new_data = new_data.drop(['Customer_ID', 'Customer_Status', 'Churn_Category', 'Churn_Reason'], axis=1)

# Encode categorical columns using previous label encoders
for column in new_data.select_dtypes(include=['object']).columns:
    if column in label_encoders:
        new_data[column] = label_encoders[column].transform(new_data[column])

# Make predictions on new data
new_probs = xgb_model.predict_proba(new_data)[:, 1]
new_predictions = (new_probs >= threshold).astype(int)

# Add predictions to original data
original_data['Customer_Status_Predicted'] = new_predictions

# Filter churned predictions
churned_customers = original_data[original_data['Customer_Status_Predicted'] == 1]

# Save results
output_path = r"C:\Users\Admin\prediction_results.csv"
churned_customers.to_csv(output_path, index=False)

print(f"\n✅ Predictions saved to {output_path}")

