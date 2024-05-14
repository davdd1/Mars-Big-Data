import streamlit as st
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import json
import random

apikey = 'Bgt2DAbyTrtQuPO1XbqtAeTzfuVAjUiViACsdkge'
st.set_page_config(layout="wide", page_title="Mars Super Smart ML", page_icon="🚀", initial_sidebar_state="auto")
col1, col2= st.columns(2)

with col1:
    welcome_sequence = """
    # :red[Vad gör vi med all denna data?] :package:


    """

    questions = """
    ## - Machine learnining :robot:
    ### *Vi använder maskininlärning för att förutsäga vädret på Mars*




    ## - Datahantering :bar_chart:
    ### *Vi samlar in, lagrar och bearbetar data för att kunna använda den i vår modell*



    """

    def stream_data():
        for char in welcome_sequence:
            yield char 


        for char in questions:
            yield char

    st.write_stream(stream_data())

with col2:
    def display_image_info(img_url):
        with open ('pages\mars_data_weather.json', 'r') as f:
            data = json.load(f)
            for photo in data['photos']: #för att veta vilken sol det är
                if photo['img_src'] == img_url:
                    rightSol = photo['sol']
                    st.write(f"Camera: {photo['camera']['full_name']}") #skriver ut kameran som användes
                    break
        #read from the csv file
        #display the min and max temp for the sol    
        df = pd.read_csv('pages\mars-weather.csv')
        for sol in df['sol']:
            if sol == rightSol:
                st.write(f"Min Temp: {df['min_temp'][sol]}", "°C")
                st.write(f"Max Temp: {df['max_temp'][sol]}", "°C")
                st.write(f"Pressure: {df['pressure'][sol]} Pa")
                st.write(f"Earth Date: {df['terrestrial_date'][sol]}")
                break    
     
    def send_image_request(sol): 
        url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol={sol}&api_key={apikey}'

        try:
            with open('pages\mars_data_weather.json', 'r') as f:
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
        with open('pages\mars_data_weather.json', 'w') as f:
            json.dump(newdata.json(), f, indent=4)

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
        with open('pages\mars_data_weather.json', 'r') as f:
            data = json.load(f)
        if (data['photos'] == []):
            st.warning("No data available")
        else:
            display_random_image(data)