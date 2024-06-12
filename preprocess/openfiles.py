import os

# Path to the directory containing the folders
directory = 'data/'

# Iterate over all items in the directory
for folder_name in os.listdir(directory):
    # Form the full folder path
    old_folder_path = os.path.join(directory, folder_name)

    # Check if the item is a folder
    if os.path.isdir(old_folder_path):
        # Capitalize the first letter of the folder name
        new_folder_name = folder_name.capitalize()
        new_folder_path = os.path.join(directory, new_folder_name)

        # Rename the folder
        os.rename(old_folder_path, new_folder_path)

print("Folder names have been capitalized.")
