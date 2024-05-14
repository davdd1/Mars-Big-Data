import streamlit as st
import time
import pandas as pd
import numpy as np
import os
st.set_page_config(layout="wide", page_title="Mars Super Smart ML", page_icon="🚀", initial_sidebar_state="auto")
welcome_sequence = """
# :red[ Målgrupp ] :raised_hand_with_fingers_splayed: :nerd_face:
"""

questions = """
## - Forskare

## - Astrofysiker

## - Dataintresserade

## - Entusiaster

"""
def stream_data():
    for char in welcome_sequence:
        yield char 
        time.sleep(0.02)

    for char in questions:
        yield char
        time.sleep(0.05)

st.write_stream(stream_data())

