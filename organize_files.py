import os
import shutil

def organize_files_by_extension(folder_path):
    # Loop through all files in the provided folder path
    for filename in os.listdir(folder_path):
        # Split the file into name and extension
        name, ext = os.path.splitext(filename)
        ext = ext[1:]  # Remove the dot from the extension

        # Skip files with no extension
        if ext == '':
            continue

        # Create a destination directory based on the extension
        dest_dir = os.path.join(folder_path, ext)
        
        # If the destination directory doesn't exist, create it
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        # Move the file to the respective directory based on its extension
        shutil.move(os.path.join(folder_path, filename), os.path.join(dest_dir, filename))

    print("Files organized by extension.")

# Prompt user to input the folder path they want to organize
folder_path = input("Enter the path to organize: ")

# Call the function to organize files
organize_files_by_extension(folder_path)
