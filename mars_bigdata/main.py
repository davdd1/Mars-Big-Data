import requests
import json
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

apikey = 'Bgt2DAbyTrtQuPO1XbqtAeTzfuVAjUiViACsdkge'
#requsta från mars apin, spara i JSon fil

#ta datan och hantera dvs visualisera i pandas dataframe

#skapa en streamlit app som visar datan

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1001&api_key=DEMO_KEY'
response = requests.get(url)
data = response.json()

with open('mars_data_weather.json', 'w') as f:
    json.dump(data, f, indent=4)


