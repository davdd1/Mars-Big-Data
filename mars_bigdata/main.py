import requests
import json
import streamlit as st
import random

apikey = 'Bgt2DAbyTrtQuPO1XbqtAeTzfuVAjUiViACsdkge'

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



sol = st.number_input("Enter a sol number:", min_value=0, max_value=1200, value=0)

confirme = st.checkbox("I confirm that I want to see the photo of the sol number entered above.")

if sol > 0 and confirme:
    url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol={sol}&api_key={apikey}'
    data = requests.get(url)
      
    with open('mars_data_weather.json', 'w') as f:
        json.dump(data.json(), f, indent=4)

    with open ('mars_data_weather.json', 'r') as f:
        data = json.load(f)    
    display_random_image(data)  # Display a single random image
    
    if st.button("Get new photo"):
        with open ('mars_data_weather.json', 'r') as f:
            data = json.load(f)
        display_random_image(data)