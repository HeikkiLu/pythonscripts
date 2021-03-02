import os
import shutil
from pathlib import Path

home = str(Path.home())
downloads_folder = home+"/Downloads/"

# List all files in downloads folder
def list_files():

    files = os.listdir(downloads_folder)
    
    for f in files:
        ext = Path(f).suffix
        try:
            if ext=='.md' or ext=='.pdf' or ext=='.docx' or ext=='.data' or ext=='.pptx':
                move_file(f, 'documents')   
            if ext=='.zip' or ext=='.jar' or ext=='.tar' or ext=='.gz' or ext=='.rar':
                move_file(f, 'zips')
            if ext=='.jpg' or ext=='.jpeg' or ext=='.png' or ext=='.tiff' or ext=='.gif':
                move_file(f, 'pictures')
            if ext=='.exe' or ext=='.deb' or ext=='.AppImage' or ext=='.sh' or ext=='.run':
                move_file(f, 'executables')
            else:
                if f=="documents" or f=="zips" or f=="pictures" or f=="executables" or f=="other":
                    pass
                else:
                    move_file(f, 'other')
        except FileNotFoundError:
            pass

# Move files to their directories
def move_file(f, d):
    new_path = shutil.move(downloads_folder + f, downloads_folder+d)
    print(f'Moved {downloads_folder + f} to {new_path}')

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
    list_files()
