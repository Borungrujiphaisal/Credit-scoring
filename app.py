import streamlit as st
import joblib
import numpy as np
import pandas as pd

st.title('Credit Score Calculator')
st.sidebar.header('Input Features')

age                             = st.sidebar.number_input('Age', min_value=18, max_value=100, value=30)
DSR                             = st.sidebar.number_input('Debt Service Ratio', min_value=0.0, value=0.3, step=0.01)
MI                              = st.sidebar.number_input('Monthly Income', min_value=0.0, value=5000.0, step=100.0)
NCLL                            = st.sidebar.number_input('Number of Open Credit Lines and Loans', min_value=0, max_value=50, value=5)
WE                              = st.sidebar.number_input('Working experince (Months)', min_value=0, max_value=10, value=12)
predict_button                  = st.sidebar.button('Predict')

if predict_button:
  
    value       = [age, DSR, MI, NCLL, WE]
    coef        = [-1.05, -0.39, -0.56, 0.95, -0.102]
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
