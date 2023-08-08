import os
folder_path = ""
entries = os.scandir(folder_path)

for entry in entries:
    if os.path.isfile(entry):
        print('File: ',entry.name)
    elif os.path.isdir(entry):
        print('Directory:',entry.name)

folder_destination = ""
newName = os.path.join(folder_destination,'new.txt')


locationOriginal = os.path.join(folder_path,'new.txt')
locationFinal = os.path.join(folder_destination,'new.txt')

os.rename(locationOriginal,locationFinal)