import streamlit as st
st.set_page_config(page_title="Ashu's saloon", page_icon="💇", layout="centered")

import pandas as pd

# Footer
footer_style = """<style> ... </style>"""
st.markdown(footer_style, unsafe_allow_html=True)

st.title("Welcome to Ashu's Saloon! 💇‍♂️💇‍♀️")

@st.cache_data
def load_data(sheet):
    return pd.read_excel("Price_list.xlsx",sheet_name=sheet.lower(),)

serv_select = ["Select Service","Threading","Waxing","Bleach","Dtan",
               "Clean up","Facials","Chemical treatment","Hair spa",
               "Haircut","Hairset"]

serv = st.selectbox("💄 Choose Service", serv_select)

if serv != "Select Service":
    df = load_data(serv)
    filtered = df

    if not filtered.empty:
        st.dataframe(filtered)
    else:
        st.warning("No data found")

