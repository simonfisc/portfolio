import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.png')

with col2:
    st.title("Simon Carrier")
    content = """Hi, I am Simon! I am a Python programmer. 
    I have worked with companies from various contries.
    """
    st.info(content)

content2 = ("""
Below you can find some of the apps I have built in Python. Feel free to contact me!
""")
st.text(content2)

df = pd.read_csv('data.csv', sep=";")
col3, empty_col_, col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    for index, row in df[::2].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[1::2].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
