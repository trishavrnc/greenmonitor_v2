import streamlit as st
from PIL import Image

icon_image = 'icon.png'

st.set_page_config(
    page_title="GreenMONitor",
    layout="wide",
    page_icon=icon_image
)
st.header("About")

with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        pass
    with col2:
        image = Image.open(icon_image)
        st.image(image, width=300)
    with col3:
        pass