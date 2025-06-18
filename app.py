
import streamlit as st #web arayuzu
import pickle #trained modeli pkl den acar
import numpy as np #ML modelleri numpy array ile çalışır/not list

st.title("🩺 Diabetes Prediction App") #st.title,st.write

#with ile dosya acilir ve file desikenine atanir 
#dosya otomatik kapatilir (with sayesinde)

with open("diabetes_model.pkl", "rb") as file: 
    model = pickle.load(file) 
#rb= read binary
#pickle.load(file)=Kaydedilen modeli dosyadan geri açmak

#slider ile veri al
glucose = st.slider("Glucose Level", 0, 200, 120)
bmi = st.slider("Body Mass Index (BMI)", 10.0, 50.0, 25.0)
age = st.slider("Age", 10, 100, 30)
pedigree = st.slider("Diabetes Pedigree Function", 0.0, 2.5, 0.5)

# Predict butonuna tıklanırsa
if st.button("Predict"):
    # Kullanıcının girdiği verileri 2D numpy array formatı yapti
    user_input = np.array([[glucose, bmi, age, pedigree]])

    prediction = model.predict(user_input)
    if prediction[0] == 1:
        st.error("⚠️ High Risk of Diabetes")
    else:
        st.success("✅ Low Risk of Diabetes")
