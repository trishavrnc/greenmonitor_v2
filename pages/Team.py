import streamlit as st
from PIL import Image

icon_image = 'icon.png'

st.set_page_config(
    page_title="GreenMONitor",
    layout="wide",
    page_icon=icon_image
)

st.header("Meet the Team")
st.markdown("<div>\n</div>", unsafe_allow_html=True)

team_images = ['images/cassie.png', 'images/charles.png', 'images/choy.png', 'images/kyle.png',
                'images/nepets.png', 'images/nica.png', 'images/pey.png']

with st.container():
    col1, col2, col3, col4, col5, col6, col7 = st.columns([2,1,2,1,2,1,2])

    with col1:
        image = Image.open(team_images[0])
        st.image(image, width=200)
        st.markdown("<h4 style='text-align:center'>Ina Cassandra Morales</h4>", unsafe_allow_html=True)
    with col2:
        pass    
    with col3:
        image = Image.open(team_images[1])
        st.image(image, width=200)
        st.markdown("<h4 style='text-align:center'>Charles Denzel Lim</h4>", unsafe_allow_html=True)
    with col4:
        pass
    with col5:
        image = Image.open(team_images[2])
        st.image(image, width=200)
        st.markdown("<h4 style='text-align:center'>Nichole Bantiling</h4>", unsafe_allow_html=True)
    with col6:
        pass
    with col7:
        image = Image.open(team_images[3])
        st.image(image, width=200)
        st.markdown("<h4 style='text-align:center'>Adriene Kyle Valencia</h4>", unsafe_allow_html=True)

with st.container():
    col1, col2, col3, col4, col5, col6, col7 = st.columns([1,2,1,2,1,2,1])

    with col1:
        pass
    with col2:
        image = Image.open(team_images[4])
        st.image(image, width=200)
        st.markdown("<h4 style='text-align:center'>Stephen Rae Domingo</h4>", unsafe_allow_html=True)
    with col3:
        pass
    with col4:
        image = Image.open(team_images[5])
        st.image(image, width=200)
        st.markdown("<h4 style='text-align:center'>Trisha Veronica Esmeria</h4>", unsafe_allow_html=True)
    with col5:
        pass
    with col6:
        image = Image.open(team_images[6])
        st.image(image, width=200)
        st.markdown("<h4 style='text-align:center'>Princess Faye Pabulayan</h4>", unsafe_allow_html=True)
    with col7:
        pass