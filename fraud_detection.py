import streamlit as st
import joblib
import pandas as pd

model = joblib.load('fraud_detection_model.pkl')
st.title('Fraud Detection App')
st.markdown('Enter the details of the transaction to predict if it is fraudulent or not.')
st.divider()

transaction_type = st.selectbox('Transaction Type', ['Payment', 'Transfer', 'Cash Out', 'Debit', 'Credit'].upper())
amount = st.number_input('Amount', min_value=0.0)
oldbalanceOrg = st.number_input('Old Balance Sender', min_value=0.0, value=10000)
newbalanceOrg = st.number_input('New Balance Sender', min_value=0.0, value=9000)

oldbalanceDest = st.number_input('Old Balance Receiver', min_value=0.0, value=0.0)
newbalanceDest = st.number_input('New Balance Receiver', min_value=0.0, value=0.0)


if st.button('Predict'):
    input_data = pd.DataFrame({
        'type': [transaction_type],
        'amount': [amount],
        'oldbalanceOrg': [oldbalanceOrg],
        'newbalanceOrg': [newbalanceOrg],
        'oldbalanceDest': [oldbalanceDest],
        'newbalanceDest': [newbalanceDest]
    })
    prediction = model.predict(input_data)
    st.subheader(f'Prediction Result: {prediction[0]}')
    if prediction[0] == 1:
        st.error('The transaction is predicted to be fraudulent.')
    else:
        st.success('The transaction is predicted to be legitimate.')