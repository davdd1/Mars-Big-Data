import streamlit as st
import time
import pandas as pd
import numpy as np

st.set_page_config(layout="wide", page_title="Mars Super Smart ML", page_icon="🚀", initial_sidebar_state="auto")
col1, col2= st.columns(2)

with col1:
    welcome_sequence = """
    # :red[Hur lagrar vi all denna data?] :package:


    """

    questions = """
    ## - Data Lake :wave:
    ### *Samlar stora mängder data från olika enheter*




    ## - Nackdelar med en data lake?
    ### *Träsk av stora mängder data*



    ## - Json och CSV
    ### *Vi använder JSON och CSV för att lagra data från Mars*



    """

    def stream_data():
        for char in welcome_sequence:
            yield char 
            time.sleep(0.02)

        for char in questions:
            yield char
            time.sleep(0.02)

    st.write_stream(stream_data())

with col2:
    #display databasbild.png on the right side
    st.image('Databasbilder2.png', use_column_width=True)
