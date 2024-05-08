import requests
import json
import streamlit as st
import random

apikey = 'Bgt2DAbyTrtQuPO1XbqtAeTzfuVAjUiViACsdkge'

def display_random_image(json_data):
    random_image = random.choice(json_data['photos'])
    img_url = random_image['img_src']
    
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