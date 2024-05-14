import streamlit as st
import time
import pandas as pd
import numpy as np
import os

st.set_page_config(layout="wide", page_title="Mars Super Smart ML", page_icon="🚀", initial_sidebar_state="auto")
col1, col2= st.columns(2)

with col1:
    welcome_sequence = """
    # :red[ Välkommna ! ] :sunglasses: :moon:

    """

    questions = """
    # Vår tanke:

    """

    idea = """
    - ## Hämta miljödata från :red[**Mars**].

    - ## Jämföra miljön på :red[**Mars**] med :green[**Jorden**].

    - ## Förutsäga vädret på :red[**Mars**] med hjälp av :gray[**Maskininlärning**].

    - ## Hämta bilder från :red[**Mars**] och analysera dem :scream:  

    """
    def stream_data():
        for char in welcome_sequence:
            yield char 
            time.sleep(0.05)

        for char in questions:
            yield char
            time.sleep(0.05)

        for char in idea:
            yield char
            time.sleep(0.02)

    st.write_stream(stream_data())

with col2:
    st.image("https://m.media-amazon.com/images/S/pv-target-images/1693a5d8c96fec05a3e1636d5c4566ac0307929fe79e8bbcdb91dda5292d142f.jpg", use_column_width=True)
