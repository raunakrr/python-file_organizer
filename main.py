import os

path = "C:\\Users\\rauna\\OneDrive\\Desktop\\dummy_folder"
file_map={".jpg":"Images",
     ".png":"Images",
     ".pdf":"Documents",
     ".txt":"Documents"}
if os.path.exists(os.path.join(path,"Images"))!=True:
    os.makedirs(os.path.join(path,"Images"))
if os.path.exists(os.path.join(path,"Documents"))!=True:
    os.makedirs(os.path.join(path,"Documents"))

for i in os.listdir(path):
    name,ext=os.path.splitext(i)
    ext=ext.lower()
    folder_name = file_map.get(ext)
    if folder_name: 
        os.replace(os.path.join(path,i),os.path.join(path,folder_name,i))
    else:
        print("skipping {"+i+"}")
   
       