import streamlit as st
import pandas as pd

from data_integration import DineSafeAPIConn

# Create the application UI
st.title("Toronto Open Data Streamlit App")

st.text(("Sample Data Set From Dinesafe"))

conn = st.experimental_connection("dinesafe-api", type=DineSafeAPIConn)
st.dataframe(conn.get_dinesafe_data(15))