import streamlit as st
import joblib
st.title('HEART DISEASE PREDICTION')
model= joblib.load('C:/chinnu/Heart_Disease_Prediction.joblib')
Age= st.number_input('Enter age')
Sex= st.number_input('Enter gender (M:1,FM:0)')
chest_paintype= st.number_input('Enter in digits')
BP= st.number_input('Enter blood pressure')
Cholesterol= st.number_input('Enter cholesterol')
FBS = st.number_input('Enter FBS(Y:1,N:0)')
EKG_results= st.number_input('Enter results')
MAX_HR= st.number_input('Enter max hr')
Exercise_agina = st.number_input('Enter exercise agina(Y:1,N:0)')
ST_depression= st.number_input('Enter st depression')
Slope_of_ST= st.number_input('Enter slope of st')
Number_of_vesselsfluro= st.number_input('Enter no of vesselsfluro')
Thallium= st.number_input('Enter thallium percentage')
if st.button('Predict Heart Disease'):
    prediction=model.predict([[Age,Sex,chest_paintype,BP,Cholesterol,FBS,EKG_results,MAX_HR,Exercise_agina,ST_depression,Slope_of_ST,Number_of_vesselsfluro,Thallium]])
    if prediction=='Y':
        st.text('Heart disease presence')
    else:
        st.text('Heart disease absence')
