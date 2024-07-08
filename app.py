import streamlit as st
import joblib
import numpy as np
import pandas as pd

st.title('Credit Score Calculator')
st.sidebar.header('Input Features')

age                             = st.sidebar.number_input('Age', min_value=18, max_value=100, value=30)
DSR                             = st.sidebar.number_input('Debt Service Ratio', min_value=0.0, value=0.3, step=0.01)
ME                              = st.sidebar.number_input('Monthly Expense', min_value=0, max_value=100000, value=15000, step=2500)
ND                              = st.sidebar.number_input('Number of Dependents', min_value=0, max_value=10, value=3)
WE                              = st.sidebar.number_input('Working experince (Months)', min_value=0, max_value=720, value=180)
predict_button                  = st.sidebar.button('Predict')

if predict_button:
  
    value       = [age, DSR, ME, ND, WE]
    coef        = [-0.022, -1.02, 0.000056, 0.095, -0.0153]
    predicted_prob = 1/(1+np.exp(-np.dot(value,coef)))
    
    st.subheader('Estimate Probability of Default')
    st.write(f'Probability of Credit Risk: {predicted_prob:.4f}')

    if predicted_prob >= 0.5:
        st.write('Action: Reject')
    elif 0.1 <= predicted_prob < 0.5:
        st.write('Action: Refer')
    else:
        st.write('Action: Approve')
        
        
if __name__ == '__main__':
    st.sidebar.info('This app is a demo for HLTC.')
