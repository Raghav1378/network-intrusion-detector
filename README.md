# 🛡️ Network Threat Detection with Machine Learning

This project uses a labeled network traffic dataset to detect threats such as bot attacks and port scans using machine learning. The model is trained on features like protocol, request type, user agent, status, and payload size. After model selection and evaluation, the final classifier is deployed via a Streamlit interface for real-time predictions.

---

## 📌 Description

The dataset simulates one week of network activity, covering both normal and malicious logs. After performing data cleaning, encoding, and scaling, various classification models were trained, including Decision Tree, Random Forest, XGBoost, and MLP. SHAP was used to interpret model predictions and analyze feature importance.

The Decision Tree model was selected for deployment due to its balance of accuracy and explainability. A simple Streamlit app was built to make real-time predictions based on user-inputted network features.

---

## 🚀 Highlights

- Full ML pipeline from raw logs to deployed model
- Exploratory data analysis to understand attack behavior
- Model evaluation using accuracy, confusion matrix, and classification report
- Feature importance analysis using SHAP
- Streamlit-based UI for live predictions

---

## 🧠 Tools & Technologies

- Python (Pandas, NumPy, Seaborn, Matplotlib)
- Scikit-learn, XGBoost, SHAP
- Streamlit for deployment
- Joblib for model persistence

---

## 🙋‍♂️ About Me

I'm Raghav Ramani, currently exploring machine learning applications in domains like network security and anomaly detection. This project helped me practice end-to-end ML workflows — from feature engineering to model deployment.

---

> ⭐ Star this repo if you find the work useful or interesting!
