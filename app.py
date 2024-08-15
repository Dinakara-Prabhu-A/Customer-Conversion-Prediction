# import pacakages
import streamlit as st
import pandas as pd
import joblib
# setup the web page title

st.set_page_config(page_title='Customer Conversion Prediction', page_icon=None, layout="centered", initial_sidebar_state="expanded", menu_items=None)
st.header('Customer Conversion Prediction',divider = 'grey')
def model_predict(main_container):
    col1,col2,col3 = main_container.columns(3,gap="medium")
    with col1:
        t_education = ('tertiary', 'secondary', 'unknown', 'primary')
        
            
        container=st.container(border = True)
        age = container.number_input("Enter the Age",min_value=18,max_value=95,value =18,key="age1")
        container=st.container(border = True)
        education  = container.selectbox("Education Status",t_education,index =None,placeholder="-- Select  --")
        


    with col2:

        t_job = ('management', 'technician', 'entrepreneur', 'blue-collar',
        'unknown', 'retired', 'admin.', 'services', 'self-employed',
        'unemployed', 'housemaid', 'student')
        
        t_call = ('unknown', 'cellular', 'telephone')

        container=st.container(border = True)
        job = container.selectbox(
            "Select the Job Type",t_job,
            index=None,
            placeholder="-- Select --",)
        
        container=st.container(border = True)
        call  = container.selectbox("contact communication type",t_call,index =None,placeholder="-- Select  --")

    with col3:
        
        t_marital = ('married', 'single', 'divorced')
        
        container=st.container(border = True)
        marital = container.selectbox("Select Marital Status",t_marital,index=None,placeholder="-- Select --",)
        
        container=st.container(border = True)
        date = container.number_input("Last contact date",min_value=1,max_value=31)
            


    with col1:
        t_mon = ('jan','feb','mar', 'apr','may', 'jun', 'jul', 'aug','sep','oct', 'nov', 'dec')
        container=st.container(border = True)
        month = container.selectbox("Last Contact Month",t_mon,index=None,placeholder="-- Select  --")

    with col2:
        container = st.container(border = True)
        num_calls = container.slider("number of contacts", 1, 100, 1)

    with col3:
        t_cam = ('unknown', 'failure', 'other', 'success')
        container=st.container(border = True)
        cam = container.selectbox("previous campaign",t_cam,index=None,placeholder="-- Select  --")
    # default mean value for dur
    with col1:
        container=st.container(border = True)
        dur = container.number_input("Last Call Duration in (sec) ",min_value=1,max_value=5000)

    columns = ['age', 'job', 'marital', 'education_qual', 'call_type', 'day', 'mon',
       'dur', 'num_calls', 'prev_outcome']
    data = [[age, job, marital, education, call, date, month, dur, num_calls, cam]]

    new_data = pd.DataFrame(data,columns = columns)
    xgb_model = joblib.load('xgb_model.pkl')
    if st.button("Submit"):
        xgb_predictions = xgb_model.predict(new_data)
        xgb_pred_proba = xgb_model.predict_proba(new_data)
        print("XGBoost Predictions:", xgb_predictions)
        print("XGBoost Prediction Probabilities:", xgb_pred_proba)
        if xgb_predictions[0] == 0:
            prediction = "No"
        else:
            prediction = "Yes"
        

        return prediction

main_container = st.container(border = True)
prediction = model_predict(main_container)
main_container = st.container(border = True)
if prediction == 'Yes':
    main_container.write("Customer is predicted to subscribe to the insurance.")
elif prediction == 'No':
    main_container.write("Customer  is predicted NOT to subscribe to the insurance.")