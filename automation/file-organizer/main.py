import os # Operating system interfaces: files, environment, processes.
import shutil # High-level file operations: copy, move, archive, disk usage.

def organize(path):
    """ Organizes a folder by filetype into new folders.
    """
    existing_folders = []

    # scan folder given folder path
    with os.scandir(path) as folder: 
         
         for file in folder:
              
              if file.is_file(): # Checks if object is a file

                if file.name.endswith(('png', 'jpeg', 'jpg')): # checks if file is an image
                    dest = os.path.join(path, 'images') # create a folder path

                    if 'images' not in existing_folders:
                        os.mkdir(dest)
                        existing_folders.append('images') # add folders to list

                    shutil.move(file.path, os.path.join(dest, file.name)) # move image file to image folder

                elif file.name.endswith(('.pdf', 'docx', 'txt')): # checks if file is a document
                    dest = os.path.join(path, 'documents')

                    if "documents" not in existing_folders:
                        os.mkdir(dest)
                        existing_folders.append('documents')
                    shutil.move(file.path, os.path.join(dest, file.name))

                elif file.name.endswith(('mp3', 'm4a')): # checks if file is a audio
                    dest = os.path.join(path, 'audio')
                    if "audio" not in existing_folders:
                        os.mkdir(dest)
                        existing_folders.append('audio')
                    shutil.move(file.path, os.path.join(dest, file.name))
                
                else:
                    # print("File is other.") # all other files are other 
                    print('This folder is organized')

    
    


filepath = "/Users/aalijahjohnson/messy-folder"

organize(filepath) 