import streamlit as st
import time
import pandas as pd
import numpy as np

st.set_page_config(layout="wide", page_title="Mars Super Smart ML", page_icon="🚀", initial_sidebar_state="auto")

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

- ## Hämta bilder från :red[**Mars**] och analysera dem

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
