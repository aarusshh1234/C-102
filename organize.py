import os
import shutil

source = "C:/Users/HP/Downloads"
destination = "C:/Users/HP/Desktop/python"
list_of_files = os.listdir(source)

#print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name) 
    #print (name)
    #print(extension)
    
    if extension == " ":
        continue
    
    if extension in [".gif", ".png", ".jpeg",".jpg", ".jfif"]:
        path1 = source+"/"+file_name
        path2 = destination+"/"+"image_files"
        path3 = destination+"/"+"image_files"+"/"+file_name

        if os.path.exists(path2):
            print("Moving "+file_name+"...")
            shutil.move(path1, path3 )
        
        else:
            os.mkdir(path2)
            print("Moving "+file_name+"...")
            shutil.move(path1, path3 )
            
