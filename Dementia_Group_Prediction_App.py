# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 17:47:37 2022

@author: somil.mehta
"""

import pandas as pd
import streamlit as st
import pickle 
from PIL import Image

pickle_in = open("dementia.pkl","rb")
dementia = pickle.load(pickle_in)  




def welcome():
    return "Welcome All"

def Dementia_Group_Prediction(Age,Visit,MR_Delay,MF,EDUC,SES,MMSE,CDR,eTIV,nWBV,ASF):
    
    prediction = dementia.predict([[Age,Visit,MR_Delay,MF,EDUC,SES,MMSE,CDR,eTIV,nWBV,ASF]])
    print(prediction)
    return prediction

    #name = st.text_input(label = "Enter Patient Name")
    #submit = st.form_submit_button(label = "Submit this Name")
def main():
    #st.title("Heart Attack Prediction")
    html_temp = """
    <div style = "background-color:tomato;padding:10px">
    <h2 style = "color:white;text-align:center;"> Dementia Group Prediction Web App </h2>
    </div>
    """
    
    
    st.markdown(html_temp,unsafe_allow_html = True)
    Age = st.text_input("Patient Age")
    Visit = st.slider("Number of Visit",min_value=1,max_value=5)
    MR_Delay = st.text_input("Number of MR Delay")
    MF = st.radio("Gender [MALE : 1 & FEMALE : 0]",(1,0))
    EDUC = st.slider("Number of EDUC",min_value=5,max_value=24)
    SES = st.slider("Number of SES", min_value = 1, max_value = 5)
    MMSE = st.slider("Number of MMSE", min_value = 4, max_value = 30) 
    CDR = st.slider("CDR",min_value=0.0, max_value = 2.0)
    eTIV = st.slider("ETIV",min_value=1106,max_value=2204)
    nWBV = st.slider("NWBV",min_value=0.644,max_value=0.837)
    ASF = st.slider("ASF",min_value = 0.876, max_value = 1.587)             
    result = ""
    if st.button("Predict"):
        result = Dementia_Group_Prediction(Age,Visit,MR_Delay,MF,EDUC,SES,MMSE,CDR,eTIV,nWBV,ASF) 
    st.success("Dementia Group : {}".format(result))
    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built with Streamlit")
        
if __name__=='__main__':
    main()        
