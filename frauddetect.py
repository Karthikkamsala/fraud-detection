# -*- coding: utf-8 -*-
"""frauddetect.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jU4TBh8ypVCW_0HYUseajf4bb8agpkuk
"""

import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split

# Load the data
data = pd.read_csv("creditcard.csv")

# Split the data into training and test sets
X = data.drop(["Class"], axis=1)
y = data["Class"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Define the Streamlit app
def app():
    st.title("Credit Card Fraud Detection")
    st.write("Upload a CSV file with the credit card transaction data to predict fraud.")
    file = st.file_uploader("Choose a CSV file", type="csv")
    if file is not None:
        test_data = pd.read_csv(file)
        predictions = model.predict(test_data)
        st.write("Predictions: ", predictions)
        st.write("Accuracy: ", accuracy_score(y_test, predictions))
        st.write("Confusion Matrix: ", confusion_matrix(y_test, predictions))

if __name__ == '__main__':
    app()