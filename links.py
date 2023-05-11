import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()



col1, col2 = st.columns(2)


st.header('Header')

st.info('bio')

icon_size = 20

st_button('youtube', 'https://atmindgroup.com/', 'Link', icon_size)
st_button('youtube', 'https://atmindgroup.com/', 'Link', icon_size)
st_button('medium', 'https://atmindgroup.com/', 'Link', icon_size)
st_button('twitter', 'https://atmindgroup.com/', 'Link', icon_size)
st_button('linkedin', 'https://atmindgroup.com/', 'Link', icon_size)
st_button('newsletter', 'https://atmindgroup.com/', 'Link', icon_size)
st_button('cup', 'https://atmindgroup.com/', 'Link', icon_size)