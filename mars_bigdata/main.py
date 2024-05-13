import requests
import json
import streamlit as st
import random
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#define the function display image info
apikey = 'Bgt2DAbyTrtQuPO1XbqtAeTzfuVAjUiViACsdkge'
st.set_page_config(layout="wide", page_title="Mars Super Smart ML", page_icon="🚀", initial_sidebar_state="auto")
col1, col2, col3 = st.columns(3)

with col2:
    def display_image_info(img_url):
        with open ('mars_data_weather.json', 'r') as f:
            data = json.load(f)
            for photo in data['photos']: #för att veta vilken sol det är
                if photo['img_src'] == img_url:
                    rightSol = photo['sol']
                    st.write(f"camera: {photo['camera']['full_name']}") #skriver ut kameran som användes
                    break
        #read from the csv file
        #display the min and max temp for the sol    
        df = pd.read_csv('mars-weather.csv')
        for sol in df['sol']:
            if sol == rightSol:
                st.write(f"Min Temp: {df['min_temp'][sol]}", "°C")
                st.write(f"Max Temp: {df['max_temp'][sol]}", "°C")
                st.write(f"pressure: {df['pressure'][sol]}")
                st.write(f"Earth Date: {df['terrestrial_date'][sol]}")
                break    
            
def send_image_request(sol): 
    url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol={sol}&api_key={apikey}'

    try:
        with open('mars_data_weather.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        st.warning("File not found")
        return  # Exit the function if the file is not found

    # Check if the request returns an empty response or no photos
    newdata = requests.get(url)
    if newdata.status_code!= 200:
        st.warning("Failed to fetch data")
        return  # Exit the function if the request fails

    if newdata.json()['photos'] == []:
        st.write("No data available for this sol")
        return  # Exit the function if no data is available for the sol

    # Update the JSON file only if new data is fetched
    with open('mars_data_weather.json', 'w') as f:
        json.dump(newdata.json(), f, indent=4)

df = pd.read_csv('mars-weather.csv') #laddar in data från mars-weather.csv
df['sol'] = df['sol'].astype(int) #skapar en ny kolumn med år
df = df.dropna(subset=['min_temp', 'max_temp']) #tar bort rader som inte är relevanta

average_pressure_by_sols = df.groupby('sol')['pressure'].mean()
average_temps_by_sols = df.groupby('sol')[['min_temp', 'max_temp']].mean()

with col1: #vänstra kolumnen
    sol = st.number_input("Enter a sol number:", min_value=0, max_value=1200, value=0)
    if sol:
        send_image_request(sol)

    def display_random_image(json_data):
        random_image = random.choice(json_data['photos'])
        img_url = random_image['img_src']
        
        try:
            response = requests.head(img_url, timeout=5)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            st.warning(f"Failed to load image: {e}")
            return
        
        st.image(img_url, width=500)
        display_image_info(img_url)
    
    if st.button("Get Image :sunglasses:"):
        with open('mars_data_weather.json', 'r') as f:
            data = json.load(f)
        if (data['photos'] == []):
            st.warning("No data available")
        else:
            display_random_image(data)
        
with col3: #högra kolumnen
    
    # Plot the average temperature by sol
    fig, ax = plt.subplots(figsize=(10, 6))
    min_temp = average_temps_by_sols['min_temp'].mean()
    plt.plot(average_temps_by_sols.index, average_temps_by_sols['min_temp'], label='Min Temp', color='blue') #graf för min temp
    plt.plot(average_temps_by_sols.index, average_temps_by_sols['max_temp'], label='Max Temp', color='red') #graf för max temp

    plt.xlabel('Sol')
    plt.ylabel('Temperature')
    plt.title('Mars Weather')
    plt.legend()
    plt.show()
    st.title('Mars Temperature / pressure')
    st.pyplot(fig)
            # Plot the average pressure by sol
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.plot(average_pressure_by_sols.index, average_pressure_by_sols, label='Pressure', color='green')
    plt.xlabel('Sol')
    plt.ylabel('Pressure')
    plt.title('Mars Weather - Pressure')
    plt.legend()
    st.pyplot(fig)

def set_background():
    #api_key = "DEMO_KEY"
    #date = "2024-05-04"
    url = "https://images.pexels.com/photos/956981/milky-way-starry-sky-night-sky-star-956981.jpeg?cs=srgb&dl=pexels-felixmittermeier-956981.jpg&fm=jpg"
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
