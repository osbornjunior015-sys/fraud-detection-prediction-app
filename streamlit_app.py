import streamlit as st
import pandas as pd
import numpy as np 
import joblib

 model = joblib.load("/content/fraud_detection_pipelie.pkl")

st.title('🤖Fraud detection prediction app')


