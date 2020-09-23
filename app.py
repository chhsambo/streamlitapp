import pandas as pd
import streamlit as st
import pydeck as pdk


@st.cache
def get_data():
    url = "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-09-12/visualisations/listings.csv"
    df = pd.read_csv(url)
    return df.head(1000)

st.title("Streamlit 101")
st.markdown("Welcome to this sample demo app. You will see some use of Streamlit.")

st.header("Airbnb NYC listing data")
df = get_data()
st.line_chart(df)

st.subheader("Show data")
cols = ["name", "host_name", "neighbourhood", "room_type", "price"]
st_cols = st.multiselect("Columns", df.columns.tolist(), default=cols)
if st_cols:
    st.dataframe(df[st_cols])
else:
    st.dataframe(df)
    
st.subheader("Map")
st.text("The following data show the Airbnb priced at $200 and above.")
st.map(df[df["price"] > 200])
