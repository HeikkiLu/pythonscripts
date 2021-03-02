import os
import shutil
from os import walk
from pathlib import Path

downloads_folder = "/home/luigi/Downloads/"

# List all files in downloads folder
def move_files():
    files = os.listdir(downloads_folder)
    
    for f in files:
        ext = Path(f).suffix
        try:
            if ext=='.md' or ext=='.pdf' or ext=='.docx' or ext=='.data' or ext=='.pptx':
                new_path = shutil.move(downloads_folder + f, f'{downloads_folder}documents')
                print(f'Moved {downloads_folder + f} to {new_path}')
            if ext=='.zip' or ext=='.jar' or ext=='.tar' or ext=='.gz' or ext=='.rar':
                new_path = shutil.move(downloads_folder + f, f'{downloads_folder}zips')
                print(f'Moved {downloads_folder + f} to {new_path}')
            if ext=='.jpg' or ext=='.jpeg' or ext=='.png' or ext=='.tiff' or ext=='.gif':
                new_path = shutil.move(downloads_folder + f, f'{downloads_folder}pictures')
                print(f'Moved {downloads_folder + f} to {new_path}')
            if ext=='.exe' or ext=='.deb' or ext=='.AppImage' or ext=='.sh' or ext=='.run':
                new_path = shutil.move(downloads_folder + f, f'{downloads_folder}executables')
                print(f'Moved {downloads_folder + f} to {new_path}')
            else:
                if f=="documents" or f=="zips" or f=="pictures" or f=="executables" or f=="other":
                    pass
                else:
                    new_path = shutil.move(downloads_folder + f, f'{downloads_folder}other')
                    print(f'Moved {downloads_folder + f} to {new_path}')

        except FileNotFoundError:
            pass

# Make directories if not present
def make_dirs():
    # Directories 
    directories = ["documents", "zips", "pictures", "executables", "other"]

    # Create directories 
    for i in directories:
        path = os.path.join(downloads_folder, i)
        try:
            os.mkdir(path)
            print(f"Created folder: {i}")
        except OSError as error:
            print(f"Folder {i} exists. Skipping.")

if __name__ == "__main__":
    print("Checking if directories exist.")
    make_dirs()
    print("Moving files.")
    move_files()
