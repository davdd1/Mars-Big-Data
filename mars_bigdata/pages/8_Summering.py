import streamlit as st
import time
import pandas as pd
import numpy as np

st.set_page_config(layout="centered", page_title="Mars Super Smart ML", page_icon="🚀", initial_sidebar_state="auto")

welcome_sequence = """
# :red[ NÅGRA FRÅGOR?] 

"""

questions = """
### (( Gäller alla utom osama ))
"""

def stream_data():
    for char in welcome_sequence:
        yield char 
        time.sleep(0.2)

    for char in questions:
        yield char
        time.sleep(1.3)

st.write_stream(stream_data())
