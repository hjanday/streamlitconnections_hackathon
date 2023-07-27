import streamlit as st
import pandas as pd

from data_integration import DineSafeAPIConn

# Create the application UI
st.title("Toronto Open Data Streamlit App")

st.text(("Sample Data Set From Dinesafe"))

conn = st.experimental_connection(name="dinesafe", type=DineSafeAPIConn)
st.write(f'{conn._connection_name()}, {conn._connect()}, {DineSafeAPIConn.get_dinesafe_data(conn, 15)}')