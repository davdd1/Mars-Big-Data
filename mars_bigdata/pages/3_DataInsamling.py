import streamlit as st
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide", page_title="Mars Super Smart ML", page_icon="🚀", initial_sidebar_state="auto")
col1, col2= st.columns(2)

with col1:
    welcome_sequence = """
    # :red[Hur samlar vi in data?] :bar_chart:


    """

    questions = """
    ## - Batch ingestion
    ### *Hämta stor mängder data i långa intervaller*



    ## - Fördel för vår modell
    ### *Vi kan använda data från tidigare observationer för att förutsäga framtida observationer*



    ## - Nackdelar?
    ### *oförutsägbara händelser kan påverka datainsamlingen*

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
    average_temps_by_sols = df.groupby('sol')[['min_temp', 'max_temp']].mean()

    fig, ax = plt.subplots(figsize=(10, 6))
    min_temp = average_temps_by_sols['min_temp'].mean()
    plt.plot(average_temps_by_sols.index, average_temps_by_sols['min_temp'], label='Min Temp', color='blue') #graf för min temp
    plt.plot(average_temps_by_sols.index, average_temps_by_sols['max_temp'], label='Max Temp', color='red') #graf för max temp

    plt.xlabel('Sol')
    plt.ylabel('Temperature')
    plt.title('Mars Weather')
    plt.legend()
    plt.show()
    st.title('Mars Temperature over time')
    st.pyplot(fig)