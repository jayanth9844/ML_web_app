import streamlit as sl
import joblib

#load a model
model=joblib.load('spam_ham_file')

#ui
sl.title("SPAM HAM DETECTOR")
ip=sl.text_input("Enter the message")

#predicting
op=model.predict([ip])
if sl.button('PREDICT'):
  sl.title(op[0]) #we get o/p
