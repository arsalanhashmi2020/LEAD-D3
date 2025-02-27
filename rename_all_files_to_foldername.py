import os

# Path to the main directory containing the folders
base_path = "C:\\Users\\Arsalan Hashmi\\Desktop\\Semester 8\\RA Work\\datasets"

# List all folders in the base path
folders = os.listdir(base_path)

for folder in folders:
    folder_path = os.path.join(base_path, folder)
    
    # Check if the current item is a folder
    if os.path.isdir(folder_path):
        # List all files in the folder (assuming only one file)
        files = os.listdir(folder_path)
        
        if len(files) == 1:
            file_path = os.path.join(folder_path, files[0])
            
            # Get the file extension
            file_extension = os.path.splitext(files[0])[1]
            
            # New file name with the parent folder's name
            new_file_name = folder + file_extension
            new_file_path = os.path.join(folder_path, new_file_name)
            
            # Rename the file
            os.rename(file_path, new_file_path)
            print(f"Renamed: {file_path} -> {new_file_path}")
        else:
            print(f"Skipping folder {folder_path} as it does not contain exactly one file.")
