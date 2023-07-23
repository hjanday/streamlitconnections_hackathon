'''
pip install streamlit, requests and json, jikanpy-v4
'''
import streamlit as st 
import requests
import json
import pandas as pd
from streamlit.connections import ExperimentalBaseConnection as EBC

	


def load_data():
    base_url = "https://ckan0.cf.opendata.inter.prod-toronto.ca"
    url = base_url + "/api/3/action/package_show"
    params = { "id": "dinesafe"}
    package = requests.get(url, params = params).json()
    
    pd_json_data = pd.read_json(package, orient='index')
    return package

st.title("Toronto Open Data Streamlit App")
data = load_data()
st.write(data)





##TODO:    
    # add connect class 
    

    # add query class to query for data
    
    
    # perform analysis
    
    
    # visualize
    
    # push to streamlit
    
    # (add app to communinty cloud)