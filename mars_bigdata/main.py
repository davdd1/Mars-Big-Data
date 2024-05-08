import requests
import json
import streamlit as st
import random
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

apikey = 'Bgt2DAbyTrtQuPO1XbqtAeTzfuVAjUiViACsdkge'


st.set_page_config(layout="wide")

sol = st.number_input("Enter a sol number:", min_value=0, max_value=1200, value=0)

df = pd.read_csv('mars-weather.csv')
df['sol'] = df['sol'].astype(int) #skapar en ny kolumn med år
df = df.dropna(subset=['min_temp', 'max_temp'])

average_temps_by_sols = df.groupby('sol')[['min_temp', 'max_temp']].mean()

sols = average_temps_by_sols.index

min_temp = average_temps_by_sols['min_temp'].mean()
max_temp = average_temps_by_sols['max_temp'].mean()

min_trend_line = np.polyfit(sols, average_temps_by_sols['min_temp'], 1)
max_trend_line = np.polyfit(sols, average_temps_by_sols['max_temp'], 1)

min_trend_func = np.poly1d(min_trend_line)
max_trend_func = np.poly1d(max_trend_line)



plt.figure(figsize=(10, 5))

plt.plot(average_temps_by_sols.index, average_temps_by_sols['min_temp'], label='Min Temp', color='blue')
plt.plot(average_temps_by_sols.index, average_temps_by_sols['max_temp'], label='Max Temp', color='red')

plt.plot(average_temps_by_sols, min_trend_func(average_temps_by_sols), "black", label='Min Temp Trend')
plt.plot(average_temps_by_sols, max_trend_func(average_temps_by_sols), "black", label='Max Temp Trend')

plt.xlabel('Sol')
plt.ylabel('Temperature')
plt.title('Mars Weather')
plt.legend()
plt.show()

st.title('Average Temperature Over the Years')
st.pyplot(plt)

def display_random_image(json_data):
    random_image = random.choice(json_data['photos'])
    img_url = random_image['img_src']
    
    try:
        response = requests.head(img_url, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        st.warning(f"Failed to load image: {e}")
        return
    
    st.image(img_url, caption=random_image['camera'], width=500)

def set_background():
    #api_key = "DEMO_KEY"
    #date = "2024-05-04"
    url = "https://apod.nasa.gov/apod/image/2405/three_ats_beletsky.jpg"
    #response = requests.get(url)
    #data = response.json()

    img_url = url

    st.markdown(
        f"""
        <style>
            .stApp {{
                background: url("{img_url}") no-repeat center center fixed;
                -webkit-background-size: cover;
                -moz-background-size: cover;
                -o-background-size: cover;
                background-size: cover;
            }}
        </style>    
        """,
        unsafe_allow_html=True
    )
set_background()




if sol > 0 :
    url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol={sol}&api_key={apikey}'  
    with open ('mars_data_weather.json', 'r') as f:
        data = json.load(f)

    if data['photos'] == []:
        data = requests.get(url)
        with open('mars_data_weather.json', 'w') as f:
            json.dump(data.json(), f, indent=4)

    elif sol != data['photos'][0]['sol']: #kollar om vi behöver hämta ny data eller ej
        data = requests.get(url)
        with open('mars_data_weather.json', 'w') as f:
            json.dump(data.json(), f, indent=4)
  
    
if st.button("Get Image :sunglasses:"):
    with open('mars_data_weather.json', 'r') as f:
        data = json.load(f)

        display_random_image(data)
         
    