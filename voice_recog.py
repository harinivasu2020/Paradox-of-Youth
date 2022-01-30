import streamlit as st
import pickle
import numpy as np
import webbrowser as wb
model = pickle.load(open('model.pkl','rb'))
def predict_crop(Age, Gender, Self_emp, family_hist, prior_treatment, work_pressure,sleep,remote_work,tech_company,social_status,care_takers_available,will_you_seek_help,leave,superviser,mental_health_data_taken,phy_health_data_taken):
    inp = np.array([[Age, Gender, Self_emp, family_hist, prior_treatment, work_pressure, sleep,remote_work,tech_company,social_status,care_takers_available,will_you_seek_help,leave,superviser,mental_health_data_taken,phy_health_data_taken]])
    prediction = model.predict(inp)
    return (prediction)

def main():
    st.title("Mental Health Assistant")
    html_temp = """
    <div style="background-color:#ED1F75 ;padding:10px">
    <h2 style="color:white;text-align:center;"> Your Health Partner  </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    Age = st.text_input("Age")
    Gender= st.text_input("Gender","1- Female 2-Male,3- Others ")
    Self_emp= st.text_input("Self_emp", "0-NO, 2-Yes")
    family_hist= st.text_input("family_hist", "0-No, 1-Yes")
    prior_treatment= st.text_input("prior_treatment", "0-No, 1-Yes")
    work_pressure= st.text_input("work pressure", "0-No, 1-Yes")
    sleep = st.text_input("sleep", "0-No, 1-Yes")
    remote_work = st.text_input("remote work", "0-No, 1-Yes")
    tech_company= st.text_input("tech company", "0-No, 1-Yes")
    social_status=st.text_input("social status", "0-No, 1-Yes")
    care_takers_available = st.text_input("care takers available", "0-Middle class, 1-Below poverty line, 2-Rich")
    will_you_seek_help= st.text_input("Will you seek help", "1-No, 2-Yes,0-depends")
    leave = st.text_input("Leave", "1-No, 2-Yes, 0-Depends")
    superviser=st.text_input("Superviser presence", "1-No, 2-Yes,")
    mental_health_data_taken= st.text_input("Have you met a therapist/doctor/psychologist", "1-No, 2-Yes")
    phy_health_data_taken=st.text_input("Physical Health Data", "1-No, 2-Yes")
    if st.button("Predict"):
        output = predict_crop(Age, Gender, Self_emp, family_hist, prior_treatment, work_pressure, sleep,remote_work,tech_company,social_status,care_takers_available,will_you_seek_help,leave,superviser,mental_health_data_taken,phy_health_data_taken)
        if output==3:
           st.success('Keep enjoying')
        elif output==2:
            st.success("Things will definitely get better... cheer up")
            wb.open("https://www.youtube.com/watch?v=_re6AX3Mi4s")
        else:
            wb.open("https://www.thelivelovelaughfoundation.org/helpline")
            wb.open_new_tab("https://www.healthyplace.com/sites/default/files/inline-images/mental-health-quote-hp-75-2_0.jpg")
            wb.open_new_tab("https://www.youtube.com/watch?v=_re6AX3Mi4s")
if __name__=="__main__":
        main()
