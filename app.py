import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

# Başlık
st.title("🩺 Diabetes Prediction App")

# Veriyi oku
df = pd.read_csv("diabetes.csv")
X = df[["Glucose", "BMI", "Age", "DiabetesPedigreeFunction"]]
y = df["Outcome"]

# Modeli eğit
model = LogisticRegression()
model.fit(X, y)

# Kullanıcıdan giriş al
glucose = st.slider("Glucose Level", 0, 200, 120)
bmi = st.slider("Body Mass Index (BMI)", 10.0, 50.0, 25.0)
age = st.slider("Age", 10, 100, 30)
pedigree = st.slider("Diabetes Pedigree Function", 0.0, 2.5, 0.5)

# Tahmin yap
if st.button("Predict"):
    user_input = np.array([[glucose, bmi, age, pedigree]])
    prediction = model.predict(user_input)

    if prediction[0] == 1:
        st.error("⚠️ High Risk of Diabetes")
    else:
        st.success("✅ Low Risk of Diabetes")
