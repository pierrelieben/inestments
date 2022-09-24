import pandas as pd
import json
import streamlit as st


def get_login_details(username, password):
    login_dict = {
        "username": username,
        "password": password
    }
    
    return login_dict