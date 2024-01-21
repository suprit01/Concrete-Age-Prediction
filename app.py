import pandas as pd
import numpy as np
import streamlit as st

import pickle as pkl


model=pkl.load(open('model.pkl','rb'))
st.header("Concrete Age Prediction")

cement=st.text_input('Enter Cement Value:')

water=st.text_input('Enter Water Value:')

strength=st.text_input('Enter Strength Value:')


features=np.array([[cement,water,strength]])

prediction=model.predict(features).reshape(-1,1)

if st.button("Get Age :"):
    st.write("Concrete Age in Days :",prediction[0])