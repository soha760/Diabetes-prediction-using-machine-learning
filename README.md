# 🏥 Diabetes Prediction Using Machine Learning

## 📌 Project Overview
This project aims to build a machine learning model that predicts whether a patient has diabetes based on clinical and demographic features.  
The system is built using data science techniques including data preprocessing, exploratory data analysis, feature engineering, model training, evaluation, and deployment using Streamlit.
---
## 📊 Dataset
- Name: Comprehensive Diabetes Clinical Dataset (100K rows)
- Dataset Download Link: https://www.kaggle.com/datasets/priyamchoksi/100000-diabetes-clinical-dataset
- Original Source: Kaggle (compiled from clinical health records / diabetes research datasets)
- Type: Medical classification dataset
- Description: Contains 100,000 patient records including demographic and clinical features such as age, gender, BMI, HbA1c level, blood glucose level, hypertension, heart disease, smoking history, and diabetes status. Used for diabetes prediction tasks.
- Target: Diabetes (0 = Non-Diabetic, 1 = Diabetic)
---
## 🤖 Machine Learning Models Used
- Logistic Regression  
- Random Forest Classifier  
- Gradient Boosting Classifier  
Best Model: Random Forest (after tuning using GridSearchCV)
---
## ⚙️ Features Engineering
- Age grouping
- BMI categorization
- Encoding categorical variables
- Feature scaling using StandardScaler
---
## 📈 Evaluation Metrics
- Accuracy  
- Precision  
- Recall  
- F1-score  
- Confusion Matrix  
---
## 🚀 Deployment
The final model is deployed using Streamlit as an interactive web application.
### 🔗 Application Links
- Local URL: http://localhost:8501  
- Network URL: http://10.94.63.231:8501  
---
## 🎥 Project Presentation Video
- Video Link: https://drive.google.com/file/d/1ecnIjA2VDM5EAuMW_1C2IgedOGJIwGkG/view?usp=sharing
---
## 👩‍🎓 Author
- Name: Soha Yehia  
## 👨‍🏫 Supervised by
- Mohamed Elsayah  
---
## 📌 How to Run Project

### 1- Install requirements
```bash
pip install -r requirements.txt
