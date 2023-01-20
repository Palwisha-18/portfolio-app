import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.jpeg')

with col2:
    st.title('Palwisha Akhtar')
    content = """ Hello 👋, I'm Palwisha!.  I am a Python Developer from Calgary, Canada.
     I am currently working at Arbisoft as a Senior Software Engineer."""

    st.info(content)

st.write("Below you can find some of the apps I have built in Python. Feel free to contact me!")


col3, col4 = st.columns(2)

df = pandas.read_csv('data.csv', sep=';')

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image(f"images/{row['image']}")
        st.write(row['url'])


with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image(f"images/{row['image']}")
        st.write(row['url'])
