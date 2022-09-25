import pandas as pd
from json import load, dump, dumps
import json
import streamlit as st
import numpy 
import os

if os.path.exists('config/login_details.json'):
    from ee_utils import *
from utils import *

st.title('EasyEquities Overview Page')

with st.form("Login", clear_on_submit=False):
    st.text_input('What is you EasyEquities username?', key = 'username')
    st.text_input('What is you EasyEquities password?', key = 'password')

    if st.session_state.username != None and st.session_state.password != None:
        username = st.session_state.username
        password = st.session_state.password
        login_dict = get_login_details(username, password)
        
        submitted = st.form_submit_button("Submit")
        if submitted:
            with open('config/login_details.json', 'w') as login:
                json.dump(login_dict, login)


overview = st.button("See accounts overview", key = 'overview')
if overview:
    st.header('Accounts')
    st.dataframe(pd.DataFrame(accounts))
    st.header('Holdings')
    st.dataframe(pd.DataFrame(holdings))
    st.header('Transactions')
    st.dataframe(pd.DataFrame(transactions))
    st.header('Valuations')
    st.json(valuations)


# Home view
# Pie chart of holdings, industries etc.
# Risk score???

# Specific holdings views 

#




