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
    col1, col2, col3 = st.columns([3,2,3])
    with col1:
        pass
    with col2:
        image = Image.open(icon_image)
        st.image(image, width=250)
    with col3:
        pass

st.markdown("<h4 style='text-align:center;'>Welcome to GreenMONitor</h4>", unsafe_allow_html=True)
st.write("Where every leaf tells a story. Upload a photo of your plant, and let our AI models do the rest. Whether you're here to identify a plant or spot an invasive species, we've got your back—because even plants need a little monitoring!")