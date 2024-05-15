import streamlit as st
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide", page_title="Mars Super Smart ML", page_icon="🚀", initial_sidebar_state="auto")
col1, col2= st.columns(2)

with col1:
    welcome_sequence = """
    # :red[Visualisering för förståelse och kommunikation] :chart_with_upwards_trend:


    """

    questions = """
    ## - Effektiv kommunikation av våra forskningsresultat
    ### *Med hjälp av grafer och diagram* 




    ## - Bibliotek för visualisering 
    ###  *Vi använder bibliotek som matplotlib och pandas för att skapa grafer -- :arrow_forward:*



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
    df = pd.read_csv('pages\mars-weather.csv') #laddar in data från mars-weather.csv
    df['sol'] = df['sol'].astype(int) #skapar en ny kolumn med år
    df = df.dropna(subset=['min_temp', 'max_temp']) #tar bort rader som inte är relevanta

    average_pressure_by_sols = df.groupby('sol')['pressure'].mean()
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.plot(average_pressure_by_sols.index, average_pressure_by_sols, label='Pressure (Pa)', color='green')
    plt.xlabel('Sol')
    plt.ylabel('Pressure (Pa)')
    plt.title('Mars Pressure by sol / time')
    plt.legend()
    st.pyplot(fig)