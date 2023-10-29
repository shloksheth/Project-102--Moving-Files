import os
import shutil

from_dir = "C:/Users/shlok/OneDrive/Desktop/directory_files"
to_dir = "C:/Users/shlok/Downloads/"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for elem in list_of_files:
    name, ext = os.path.splitext(elem)
    if ext == "":
        continue
    if ext in [ '.txt', '.doc', '.docx', '.pdf', '.jpg']:
        path1 = from_dir+"/"+elem
        path2 = to_dir+"/"+"Document Files"
        path3 = to_dir+"/"+"Document Files"+"/"+elem
        if os.path.exists(path2):
            print("Moving ",elem,"! =D")
            shutil.move(path1, path3)
        else: 
            os.makedirs(path2)
            print("Moving ",elem,"! =D")
            shutil.move(path1, path3)


