import streamlit as st
import pandas as pd
DATE_COLUMN = 'date/time'
DATA_URL = 'data/df_proccessed.csv'

def load_data(nrows):
    data = pd.read_csv(DATA_URL)
    # lowercase = lambda x: str(x).lower()
    # # data.rename(lowercase, axis='columns', inplace=True)
    # # data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data = pd.read_csv(DATA_URL)
st.title('Coffee dataset explorer')
st.subheader('Dataframe')

st.subheader('Raw data')
st.write(data)