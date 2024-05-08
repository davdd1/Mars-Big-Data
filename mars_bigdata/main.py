import requests
import json
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import random

apikey = 'Bgt2DAbyTrtQuPO1XbqtAeTzfuVAjUiViACsdkge'
#requsta från mars apin, spara i JSon fil

#ta datan och hantera dvs visualisera i pandas dataframe

#skapa en streamlit app som visar datan

#url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1001&api_key=DEMO_KEY'
#response = requests.get(url)
#data = response.json()

#with open('mars_data_weather.json', 'w') as f:
    #json.dump(data, f, indent=4)

# Initialize session state for the current image index
# Initialize session state for the current image index
# Set the page layout to wide to give more space for the image
st.set_page_config(layout="wide")

def set_background():
    api_key = "DEMO_KEY"
    date = "2024-05-04"
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date={date}"
    response = requests.get(url)
    data = response.json()

    img_url = data["url"]

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


# Initialize session state for the current image index
if 'current_image_index' not in st.session_state:
    st.session_state.current_image_index = 0

# Load JSON data
with open('mars_data_weather.json', 'r') as f:
    json_data = json.load(f)

# Get a list of photos
photolinks = [photo['img_src'] for photo in json_data['photos']]


# Dynamically adjust the number of columns based on the number of images
num_images = len(photolinks)
cols = st.columns(1)  # Adjust the number of columns to match the number of images

# Button to show the next image
if st.button('Next Image'):
    # Select a random image from the list
    st.session_state.current_image_index = random.randint(0, num_images - 1)

# Display the current image
if st.session_state.current_image_index < num_images:
    img_url = photolinks[st.session_state.current_image_index]
    for url in json_data['photos']:
        if url['img_src'] == img_url:
            cameraname = url['camera']['full_name']
            break
        else:
            cameraname = 'No camera name found'
    
    # Check if the image URL is valid and accessible
    try:
        response = requests.head(img_url, timeout=5)
        response.raise_for_status()  # Raises an HTTPError if the response status code is 4XX or 5XX
    except requests.exceptions.RequestException as e:
        # If the request fails, skip displaying the image
        st.warning("Failed to load image: {}".format(e))
        # This line is removed as it's not applicable in this context
    
    # Display the image with a width of 250, Streamlit will adjust the height
    # Use markdown to apply custom CSS for positioning
    #padding top 0 should always be 10 pixels from the left
    st.markdown("""
        <style>
           .block-container {padding-left: 10px!important}     
        </style>
    """, unsafe_allow_html=True)
    cols[0].image(img_url, caption=str(cameraname), width=500)