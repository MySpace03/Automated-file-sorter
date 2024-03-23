import os, shutil

path = r"D:/just testing for project/"

files  = os.listdir(path)

folder_name = ['Document','media files']

for i in range(len(folder_name)):
    if not os.path.exists(path + folder_name[i]):
        os.makedirs(path + folder_name[i])

for file in files:
    if ".csv" in file and not os.path.exist(path + "Document/"+file):
        shutil.move(path + file, path+"Document/"+ file)