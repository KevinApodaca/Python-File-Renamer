# The script should be in the same folder containing the file containing names and folder containing files
# Or you can pass the paths accordingly

import os

folder_with_files = input("Folder containing files: ")
file_with_names = input("File containing names: ")

if os.path.isdir(folder_with_files) and os.path.isfile(file_with_names):
    f = open(file_with_names, 'r')
    file_names = f.readlines()
    f.close()

    files = sorted(os.listdir(folder_with_files))
    if len(files) != len(file_names):
        print("Number of files and filenames do not match. Please check for errors.")
    else:
        for i in range(0,len(file_names)):
            os.rename(folder_with_files + "/" +  files[i],folder_with_files + "/" +  file_names[i].rstrip())
        print("Finished renaming.")
