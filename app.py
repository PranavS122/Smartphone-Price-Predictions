import pandas as pd
import streamlit as st
import pickle
import numpy as np


# import the model
pipe=pickle.load(open(r"pipe.pkl",'rb'))
df = pickle.load(open(r"mobile_df.pkl",'rb'))

st.title("Smartphone Price Predictor")

# brand
Company = st.selectbox("Select the Model",['ASUS','Google', 'Infinix', 'IQOO', 'LAVA', 'Micromax', 'Mi', 'MOTOROLA', 'Nokia', 'Nothing', 'OPPO', 'OnePlus', 'POCO', 'Realme', 'REDMI', 'SAMSUNG', 'Tecno', 'itel', 'vivo', 'Xiaomi'])

# colour
color_group = st.selectbox('Colour of the Model',['Black','Blue','Brown','Green','Grey','Orange','Other','Red','Silver','White','Yellow'])

# Ram
Ram = st.selectbox('Select the Ram of the variant (GB)',df["Ram"].unique())

# Storage capacity
Storage = st.selectbox('Select the Storage Capacity of the variant (GB)',df["Storage"].unique())

#Expandable options
Expandable = st.selectbox('Select the Expandable Capacity (GB / TB)',df["Expandable"].unique())

# Processor Brand 
processor_category = st.selectbox('Select the Processor of the Variant Capacity',['Exynos processor','Google Tensor processor','Helio processor','Mediatek processor','Other processor','Qualcomm processor','Unisoc processor'])

# screen size
display_inches = st.number_input('Screen Size of the model (cm)')

# screen size
Num_camera = st.selectbox('Number of Cameras', df["Num_camera"].unique())

# Battery Capacity
battery_mah = st.number_input('Battery Capacity of the model (mah)')


if st.button('Predict Price'):
    # query

    if Company == 'ASUS':
        Company = 0
    elif Company == 'Google':
        Company = 1
    elif Company == 'Infinix':
        Company = 2
    elif Company == 'IQOO':
        Company = 3
    elif Company == 'LAVA':
        Company = 4
    elif Company == 'Micromax':
        Company = 5
    elif Company == 'Mi':
        Company = 6
    elif Company == 'MOTOROLA':
        Company = 7
    elif Company == 'Nokia':
        Company = 8
    elif Company == 'Nothing':
        Company = 9
    elif Company == 'OPPO':
        Company = 10
    elif Company == 'OnePlus':
        Company = 11
    elif Company == 'POCO':
        Company = 12
    elif Company == 'Realme':
        Company = 13
    elif Company == 'REDMI':
        Company = 14
    elif Company == 'SAMSUNG':
        Company = 15
    elif Company == 'Tecno':
        Company = 16
    elif Company == 'itel':
        Company = 17
    elif Company == 'vivo':
        Company = 18
    elif Company == 'Xiaomi':
        Company = 19
    else:
        Company = None

    if color_group == 'Black':
     color_group = 0
    elif color_group == 'Blue':
        color_group = 1
    elif color_group == 'Brown':
        color_group = 2
    elif color_group == 'Green':
        color_group = 3
    elif color_group == 'Grey':
        color_group = 4
    elif color_group == 'Orange':
        color_group = 5
    elif color_group == 'Other':
        color_group = 6
    elif color_group == 'Red':
        color_group = 7
    elif color_group == 'Silver':
        color_group = 8
    elif color_group == 'White':
        color_group = 9
    elif color_group == 'Yellow':
        color_group = 10
    else:
        color_group = None



    if processor_category == 'Exynos processor':
        processor_category = 0
    elif processor_category == 'Google Tensor processor':
        processor_category = 1
    elif processor_category == 'Helio processor':
        processor_category = 2
    elif processor_category == 'Mediatek processor':
        processor_category = 3
    elif processor_category == 'Other processor':
        processor_category = 4
    elif processor_category == 'Qualcomm processor':
        processor_category = 5
    elif processor_category == 'Unisoc processor':
        processor_category = 6
    else:
        processor_category = None 

    query = np.array([Company, color_group, Ram, Storage, Expandable, processor_category, display_inches, Num_camera, battery_mah])

    query = query.reshape(1,9)

    predicted_price = int(np.round(pipe.predict(query)[0]))
    formatted_price = '{:,}'.format(predicted_price)
    st.title("The predicted price of this configuration of the mobile is " + formatted_price + " Rs.")

   

    