import streamlit as st
st.set_page_config(page_title="Ashu's saloon", page_icon="logo.png", layout="centered")

import pandas as pd

import base64

def get_base64(img_path):
    with open(img_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

img = get_base64("logo.png")

st.markdown(f"""
    <div style="display:flex; justify-content:center;">
        <img src="data:image/png;base64,{img}" height="250px" alt="Logo">
    </div>
""", unsafe_allow_html=True)
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(315deg, #1e3c72, #2a5298,skyblue);
            background-attachment: flex;
        }
    </style>
""", unsafe_allow_html=True)

# Footer
footer_style = """<style> ... </style>"""
st.markdown(footer_style, unsafe_allow_html=True)

sidebar=st.sidebar.markdown("")
sidebar.radio("I am a", ["Admin","Customer"], horizontal=True)
@st.cache_data
def load_data(sheet):
    return pd.read_excel("Price_list.xlsx",sheet_name=sheet.lower(),)

serv_select = ["Select", "dir","Threading","Waxing","Bleach","Dtan",
               "Clean up","Facials","Chemical treatment","Hair spa",
               "Haircut","Hairset"]

serv = sidebar.radio("💄 Choose Service", serv_select,horizontal=True)
st.markdown("""
<style>
div[data-baseweb="select"] input {
    display: none;
}
</style>
""", unsafe_allow_html=True)
if serv != "Select" and serv != "dir":
    df = load_data(serv)
    filtered = df

    if not filtered.empty:
        st.dataframe(filtered)
    else:
        st.warning("No data found")
import os

if serv == "dir":
    st.write(os.listdir())
