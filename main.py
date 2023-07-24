'''
pip install streamlit, requests and json
'''
import streamlit as st 
import requests
import json
import pandas as pd
from io import StringIO
from streamlit.connections import ExperimentalBaseConnection as EBC

	


def load_data(nrows):
    base_url = "https://ckan0.cf.opendata.inter.prod-toronto.ca"
    url = base_url + "/api/3/action/package_show"
    params = { "id": "dinesafe"}
    package = requests.get(url, params = params).json()
    dumped_data = None
    for idx, resource in enumerate(package["result"]["resources"]):
    
        # for datastore_active resources:
        if resource["datastore_active"]:
    
            # To get all records in CSV format:
            url = base_url + "/datastore/dump/" + resource["id"]
            dumped_data = requests.get(url).text
            
    pd_read_data = pd.read_csv(StringIO(dumped_data)) 
    pd_read_data.rename(columns={"Latitude": "lat", "Longitude": "lon"}, inplace=True)     
    return pd_read_data.head(nrows)



st.title("Toronto Open Data Streamlit App")

st.text(("Sample Data Set From Dinesafe"))
data = load_data(100000)
print(data)

st.dataframe(data)

st.subheader("Mapped Data")
st.map(data, latitude = data["lat"], longitude = data["lon"])





##TODO:    
    # add connect class 
    

    # add query class to query for data
    
    
    # perform analysis
    
    
    # visualize
    
    # push to streamlit
    
    # (add app to communinty cloud)