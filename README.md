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
   ```
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   streamlit run app.py
   ```

---

## 🚧 Deployment Note

In the initial version, the model was trained and saved using `pickle` in a separate `model.py` file, and then loaded into the Streamlit app via a `.pkl` file.  

However, when deployed on **Streamlit Cloud**, this approach caused loading issues — the app could not access the pickled model file properly.

### ✅ Solution:
The model training process was moved directly into the `model.py` file, and the Streamlit app (`app.py`) now imports the trained model from there, ensuring full compatibility with cloud-based deployment.

---

## 🧩 Scrum Methodology (Simplified)

This project was developed in a single day with the help of AI tools (ChatGPT), and later structured into 3 basic sprints to demonstrate understanding of Agile/Scrum practices.

| Sprint    | Goal                                                  |
|-----------|-------------------------------------------------------|
| Sprint 1  | Project idea defined and dataset prepared             |
| Sprint 2  | Logistic Regression model trained in `model.py`       |
| Sprint 3  | Streamlit app built, tested, and deployed on the web  |

> Scrum artifacts (e.g., backlog, stand-up notes) are documented in `SCRUM.md` in this repository.
