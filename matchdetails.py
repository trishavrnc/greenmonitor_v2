import pandas as pd
import os
from PIL import Image
import matplotlib.pyplot as plt
import random

df = pd.read_csv('plantae.csv')

def get_invasive_species_by_family(family): # DISPLAY INVASIVE SPECIES, IF NONE, RETURN 0
    family_df = df[df['family'] == family]
    
    invasive_species = family_df[family_df['isInvasive'] == 'Invasive']
    
    invasive_species_names = invasive_species['scientificName'].tolist()
    
    if invasive_species_names:
        return invasive_species_names
    else:
        return 0

def display_images(family): # DISPLAY 3 IMAGES OF INPUT
    images_dir = os.path.join('data', family)
    
    # image_files = os.listdir(images_dir)
    
    # return [os.path.join(images_dir, image_files[i]) for i in range(min(3, len(image_files)))]

    # Check if the directory exists
    if not os.path.exists(images_dir):
        print(f"Directory {images_dir} does not exist")
        return []
    
    image_files = os.listdir(images_dir)
    
    # Shuffle the list to get random images
    random.shuffle(image_files)

    # Debugging: print the list of found images
    print(f"Found image files: {image_files}")

    # Return paths to up to 3 random images of invasive species
    return [os.path.join(images_dir, image_files[i]) for i in range(min(3, len(image_files)))]

# family_input = 'Malpighiales' # SAMPLE INPUT

# image_paths = display_images(family_input) # SAMPLE RETRIEVE PICS
# for image_path in image_paths:
#     image = Image.open(image_path)
#     plt.imshow(image)
#     plt.axis('off')
#     plt.show()

# invasive_species_list = get_invasive_species_by_family(family_input) # SAMPLE DISPLAY INVASIVE SPECIES
# if invasive_species_list != 0:
#     print("Invasive species in the family", family_input, ":", invasive_species_list)
# else:
#     print("No invasive species found for the given family.")