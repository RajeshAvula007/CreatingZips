'''
Created on Apr 15, 2019

@author: admin
'''
import zipfile
import os
import shutil


files = os.listdir()
#print(files)

for folderName in files:
    if ".zip" not in folderName and ".py" not in folderName and folderName != '__pycache__':
        #print(folderName)
        os.chdir(folderName)
        with zipfile.ZipFile(folderName+".zip", 'a') as zip1:
            
            #print("==========================")
            for contents in os.listdir():
                if ".zip" not in contents:
                    zip1.write(contents)
        os.chdir('../')
        shutil.move(folderName+'/'+folderName+".zip", ".")   
    else:
        pass