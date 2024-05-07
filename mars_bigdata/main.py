import requests
import json
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

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
cols = st.columns(num_images)  # Adjust the number of columns to match the number of images

# Button to show the next image
if st.button('Next Image'):
    st.session_state.current_image_index += 1
    if st.session_state.current_image_index >= num_images:
        st.session_state.current_image_index = 0  # Reset to the first image if we reach the end

# Display the current image
if st.session_state.current_image_index < num_images:
    img_url = photolinks[st.session_state.current_image_index]
    
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
    st.markdown("""
        <style>
           .block-container {padding-top: 0!important;}
        </style>
    """, unsafe_allow_html=True)
    cols[st.session_state.current_image_index].image(img_url, caption='Picture FROM MARS!', width=250)