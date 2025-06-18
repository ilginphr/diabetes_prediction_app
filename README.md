# 🩺 Diabetes Prediction App
https://diabetespredictionapp-ilginphr.streamlit.app/

This is a simple machine learning web app that predicts whether a person is likely to have diabetes based on health information such as glucose level, BMI, age, and family history.

The app is built using Python, trained with a logistic regression model, and deployed as an interactive web application using **Streamlit**.

---

## 🚀 Features

- User-friendly web interface (via Streamlit)
- Collects four health metrics from the user:
  - Glucose Level
  - Body Mass Index (BMI)
  - Age
  - Diabetes Pedigree Function (family history score)
- Predicts diabetes risk using a logistic regression model
- Real-time results shown with visual feedback:
  - ✅ Low Risk
  - ⚠️ High Risk

---

## 🧠 Technologies Used

| Purpose              | Library           |
|----------------------|-------------------|
| Web Interface        | `streamlit`       |
| Data Handling        | `pandas`, `numpy` |
| Machine Learning     | `scikit-learn`    |

---

## 📂 Files

| File              | Description                                 |
|-------------------|---------------------------------------------|
| `diabetes.csv`    | Dataset containing health-related features  |
| `model.py`        | Script for training and testing the model   |
| `app.py`          | Streamlit app interface (final version)     |
| `requirements.txt`| List of required Python packages            |

---

## 📌 How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/ilginphr/diabetes_prediction_app.git
cd diabetes_prediction_app

## 🚀 How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/ilginphr/diabetes_prediction_app.git
   cd diabetes_prediction_app
