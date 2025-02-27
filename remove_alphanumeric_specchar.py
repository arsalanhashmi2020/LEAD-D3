import os
import re

# Path to the main directory containing the folders
base_path = "C:\\Users\\Arsalan Hashmi\\Desktop\\Semester 8\\RA Work\\datasets"

# List all items in the base path
folders = os.listdir(base_path)

for folder in folders:
    folder_path = os.path.join(base_path, folder)
    
    # Check if the current item is a folder
    if os.path.isdir(folder_path):
        # Clean the folder name by removing invalid characters
        cleaned_folder_name = re.sub(r'[^a-zA-Z0-9\(\)\-\s]', '', folder)

        
        # Rename the folder if the cleaned name is different
        if cleaned_folder_name != folder:
            cleaned_folder_path = os.path.join(base_path, cleaned_folder_name)
            
            # Rename the folder
            os.rename(folder_path, cleaned_folder_path)
            print(f"Renamed: {folder} -> {cleaned_folder_name}")
        else:
            print(f"No change needed for folder: {folder}")
