import pandas as pd
from sklearn.model_selection import train_test_split # %80 train %20 test 
from sklearn.linear_model import LogisticRegression #0 ve 1 yani binary classification
from sklearn.metrics import accuracy_score  #predicitonun dogruluk orainin olcer
import pickle
df=pd.read_csv("diabetes.csv")
X = df[["Glucose", "BMI", "Age", "DiabetesPedigreeFunction"]]  # input
y = df["Outcome"]  # Tahmin edilecek değer 0 or 1
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)

with open("diabetes_model.pkl", "wb") as file: #wb=writebinary
    pickle.dump(model, file)
    #pickle.dump()=	Eğitilmiş modeli dosyaya kaydetmek