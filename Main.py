import streamlit as st
from PIL import Image
from runmodel_resnet import classify_images_resnet
from runmodel_mobilenetv3 import classify_images_mobilenet3
from matchdetails import get_invasive_species_by_family, display_images


def resize_image_square(image, size):
    width, height = image.size
    new_size = (size, size)
    resized_image = image.resize(new_size)
    return resized_image

def fam_name():
    # Extract the family name from the classification result
    family_name = result.split("\n")[1].split(". ")[1].split(" with")[0]

    # Get invasive species by family
    invasive_species_list = get_invasive_species_by_family(family_name)
    if invasive_species_list != 0:
        st.markdown(f"<h3 style='text-align=center;'> Invasive species in the family {family_name}: </h3>", unsafe_allow_html=True)
        st.write(invasive_species_list)
    else:
        st.markdown(f"<h4 style='text-align=center;'>No invasive species found {family_name}. </h4>", unsafe_allow_html=True)

    # Display sample images for the family
    st.markdown("<h4 style='text-align:center'>Sample Images</h4>", unsafe_allow_html=True)
    image_paths = display_images(family_name)

    for image_path in image_paths:
        image = Image.open(image_path)
        square_img = resize_image_square(image, size=300)
        st.image(square_img, caption=image_path, use_column_width=True)

icon_image = 'icon.png'

st.set_page_config(
    page_title="GreenMONitor",
    layout="wide",
    page_icon=icon_image
)

st.sidebar.success("Select a page above")

left_column, right_column, other_column = st.columns(3)

with left_column:
    st.header("Source Image")
    source = st.radio("Get image from", ["Upload", "Camera"])

    if source == "Camera":
        source_img = st.camera_input("Take a picture from camera")
    elif source == "Upload":
        source_img = st.file_uploader("Upload an image here", type=['png', 'jpg', 'jpeg', 'bmp'])
        
        # Display Image
        if source_img is not None:
            image = Image.open(source_img)
            st.image(image, caption='Uploaded Image', use_column_width=True)
    else:
        st.write("No image stored.")
        source_img = None

if st.button("Start"):
    with right_column:
        st.header("Predicted using Resnet50")
        if source_img is not None:
            result = classify_images_resnet(source_img)
            st.write(result)
            fam_name()


    with other_column:
        st.header("Predicted using MobileNetV3Large")
        result = classify_images_mobilenet3(source_img)
        st.write(result)
        fam_name()