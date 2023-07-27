'''
pip install streamlit, requests and json
'''
import streamlit as st 
import requests
import json
import pandas as pd
from io import StringIO
from streamlit.connections import ExperimentalBaseConnection
from streamlit.runtime.caching import cache_data

	
class DineSafeAPIConn(ExperimentalBaseConnection):
    def return_url(self) -> str:
        base_url = "https://ckan0.cf.opendata.inter.prod-toronto.ca"
        return base_url
    
    def _connect(self) -> requests.Session:
        session = requests.Session()
        return session

    # def conn_object(self):
    #     return self._connect()

    
    def get_dinesafe_data(self, nrows) -> pd.DataFrame:
        url = self.return_url() + "/api/3/action/package_show"
        params = { "id": "dinesafe"}
        package = requests.get(url, params = params).json()
        
        dumped_data = None
        for idx, resource in enumerate(package["result"]["resources"]):
        # for datastore_active resources:
            if resource["datastore_active"]:
        
                # To get all records in CSV format:
                url = self.return_url() + "/datastore/dump/" + resource["id"]
                dumped_data = self._instance.get(url).text
            
        pd_read_data = pd.read_csv(StringIO(dumped_data)) 
        pd_read_data.rename(columns={"Latitude": "lat", "Longitude": "lon"}, inplace=True)
        return pd_read_data.head(15)



