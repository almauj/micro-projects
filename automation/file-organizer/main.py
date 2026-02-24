import os # Operating system interfaces: files, environment, processes.
import shutil # High-level file operations: copy, move, archive, disk usage.

def organize(path):

    # scan folder given folder path
    with os.scandir(path) as folder: 
         
         for file in folder:
              
              if file.is_file(): # Checks if object is a file

                if file.name.endswith(('png', 'jpeg', 'jpg')): # checks if file is an image
                    dest = os.path.join(path, 'images') 
                    
                elif file.name.endswith(('.pdf', 'docx', 'txt')): # checks if file is a document
                    dest = os.path.join(path, 'documents')

                elif file.name.endswith(('mp3', 'm4a')): # checks if file is a audio
                    dest = os.path.join(path, 'audio')
                
                else:
                    dest = os.path.join(path, 'other') # if file not in specified format, other

                if not os.path.exists(dest):
                    os.mkdir(dest)

                shutil.move(file.path, os.path.join(dest, file.name)) # move image file to image folder


    
filepath = input('Input Folder Path >  ')

organize(filepath) 