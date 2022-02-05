import os

import streamlit as st

import random
from IPython.display import clear_output, display



import pandas as pd
import seaborn as sn
import numpy as np
import pickle
from sklearn.ensemble import ExtraTreesRegressor
from sklearn import metrics
import warnings
warnings.filterwarnings("ignore")


def Predict(input1,input2,input3):

  d = {'Height (cm)' : [input1],'Weight (kgs)' : [input2],'Age' : [input3]}
  test_df = pd.DataFrame(data= d)
  with open('Final_Model_New.pkl', 'rb') as file:
    pickle_model_new = pickle.load(file)
  result = pickle_model_new.predict(test_df)

  return result





def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:purple;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Waist Prediction ML App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 

    user_input1 = st.number_input('Height (cm)')
    user_input2 = st.number_input('Weight (kgs)')
    user_input3 = st.number_input('Age')
    result =""
      
    if st.button("Predict"): 
        result = Predict(user_input1,user_input2,user_input3)
        result_new = float(result)
        st.write('Predicted Waist Size is %.2f' % result)
    
if __name__=='__main__': 
    main()