import pandas as pd
import streamlit as st
import datetime
#from PIL import Image

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

st.title("Viajes de UBER en NY")

data = load_data(1000)

#image = Image.open(r'/Users/sofiaalmeraya/Desktop/ActM1/WALMART/Uber.png')

st.sidebar.header('**Syafiq Web App**')
st.sidebar.subheader('A01283713')

#st.sidebar.image(image,width=250)

# Some number in the range 0-23
hour_to_filter = st.sidebar.slider('Hora', 0, 23, 12)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Los viajes a las %s:00' % hour_to_filter)
st.map(filtered_data)