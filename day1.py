import os
path=r"D:\project"
number_of_files=0
number_of_folders=0
folders=[]
files=[]
# print(os.listdir(path))
for file in os.listdir(path):
    fullpath=os.path.join(path,file)
    if os.path.isdir(fullpath):
        size=os.path.getsize(fullpath)
        print(f"folder : {file} and size : {size}")
        number_of_folders+=1
        folders.append({file: size})
    elif os.path.isfile(fullpath):
        size=os.path.getsize(fullpath)

        print(f"File : {file} and the size : {size}")
        number_of_files+=1
        files.append({file: size})
print (f"Number of files is : {number_of_files} and they are : {files}")
print (f"Number of folders is : {number_of_folders} and they are : {folders}")

