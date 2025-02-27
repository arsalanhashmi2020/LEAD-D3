import os
import re

def sanitize_filename(filename):
    # Allow only alphanumeric, spaces, parentheses, and hyphens
    return re.sub(r'[^a-zA-Z0-9()\-]', '_', filename)

def rename_files_in_folder(root_folder):
    for foldername, subfolders, filenames in os.walk(root_folder):
        for filename in filenames:
            sanitized_name = sanitize_filename(filename)
            old_path = os.path.join(foldername, filename)
            new_path = os.path.join(foldername, sanitized_name)
            
            if old_path != new_path:
                os.rename(old_path, new_path)
                print(f'Renamed: {old_path} -> {new_path}')

if __name__ == "__main__":
    target_folder = r"C:\Users\Arsalan Hashmi\Desktop\Semester 8\RA Work\datasets"
    rename_files_in_folder(target_folder)
