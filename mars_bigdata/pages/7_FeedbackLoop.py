import streamlit as st
import time
import pandas as pd
import numpy as np

st.set_page_config(layout="wide", page_title="Mars Super Smart ML", page_icon="🚀", initial_sidebar_state="auto")
col1, col2= st.columns(2)

with col1:
    welcome_sequence = """
    # :red[Dem 5 V'na] :hourglass_flowing_sand:


    """

    questions = """
    # Volume: 
    ### *Stora mängder data från sensorer på Mars kräver effektiv lagring och hantering för att säkerställa tillgänglighet och bevarande.*

    # Variety: 
    ### *Integrering av olika datakällor som bilder från solsystemet (JSON) och miljöinformation (CSV) ger en mer omfattande förståelse av Mars.*

    # Velocity: 
    ### *Snabb överföring av data från Mars till jorden möjliggörs genom servrar och satelliter för nära realtidsanalys.*

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
    slide2 = """
    # Veracity: 
    ### *Många sensorer och maskininlärning används för att säkerställa noggrannhet och tillförlitlighet hos den insamlade datan.*

    # Value: 
    ### *Genom att analysera data kan vi förutspå Mars klimat, identifiera trender och bedöma möjligheterna till liv på planeten, vilket informerar framtida utforskning och kolonisering.*


    """

    def stream_data():

        for char in slide2:
            yield char
            time.sleep(0.02)



    st.write_stream(stream_data())