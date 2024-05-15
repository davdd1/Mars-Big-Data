import streamlit as st
import time
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
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

    # Prepare the data
    X = average_temps_by_sols.index.values.reshape(-1, 1)  # Features
    y_min = average_temps_by_sols['min_temp'].values  # Target for min temp
    y_max = average_temps_by_sols['max_temp'].values  # Target for max temp

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y_min, test_size=0.2, random_state=42)

    # Train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions
    predictions = model.predict(X_test)
    # Plot the original vs predicted values
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(X_test, y_test, color='blue', label='Actual')
    ax.plot(X_test, predictions, color='red', label='Predicted')
    ax.set_xlabel('Sol')
    ax.set_ylabel('Min Temp')
    ax.set_title('Mars Min Temp Prediction')
    ax.legend()
    st.pyplot(fig)  # Use st.pyplot() to display the plot in Streamlit

    # Repeat for Max Temp
    X_train, X_test, y_train, y_test = train_test_split(X, y_max, test_size=0.2, random_state=42)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print(f"Mean Squared Error for Max Temp: {mse}")

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(X_test, y_test, color='blue', label='Actual')
    ax.plot(X_test, predictions, color='red', label='Predicted')
    ax.set_xlabel('Sol')
    ax.set_ylabel('Max Temp')
    ax.set_title('Mars Max Temp Prediction')
    ax.legend()
    st.pyplot(fig)  # Use st.pyplot() to display the plot in Streamlit