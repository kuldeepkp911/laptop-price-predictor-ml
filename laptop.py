import streamlit as st
import pickle
import pandas as pd
import numpy as np

# load data and model
df = pickle.load(open('df.pkl', 'rb'))
pipe = pickle.load(open('pipe.pkl', 'rb'))

st.title("Laptop Price Predictor")

# INPUTS
company = st.selectbox('Brand', df['Company'].unique())
typename = st.selectbox('Type', df['TypeName'].unique())
ram = st.selectbox('RAM (in GB)', [2,4,6,8,12,16,24,32,64])
weight = st.number_input('Weight of the Laptop')
touchscreen = st.selectbox('Touchscreen', ['No','Yes'])
IPS = st.selectbox('IPS', ['No','Yes'])

screen_size = st.number_input('Screen Size (in inches)', min_value=1.0)
resolution = st.selectbox(
    'Screen Resolution',
    ['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440']
)

cpu = st.selectbox('CPU', df['Cpu brand'].unique())
hdd = st.selectbox('HDD (in GB)', [0,128,256,512,1024,2048])
ssd = st.selectbox('SSD (in GB)', [0,8,128,256,512,1024])
gpu = st.selectbox('GPU', df['Gpu_brand'].unique())
os = st.selectbox('os', df['os'].unique())

# 
if st.button('Predict Price'):

    # convert categorical to numeric
    touchscreen = 1 if touchscreen == 'Yes' else 0
    IPS = 1 if IPS == 'Yes' else 0

    # compute ppi
    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5 / screen_size

    # CREATING DATAFRAME 
    query = pd.DataFrame({
        'Company': [company],
        'TypeName': [typename],
        'Ram': [ram],
        'Weight': [weight],
        'Touchscreen': [touchscreen],
        'IPS': [IPS],
        'ppi': [ppi],
        'Cpu brand': [cpu],
        'HDD': [hdd],
        'SSD': [ssd],
        'Gpu_brand': [gpu],
        'os': [os]
    })

    # prediction
    price = int(np.exp(pipe.predict(query)[0]))

    st.title(f"💻 Predicted Price: ₹{price:,}")