'''
Created on Mar 14, 2019

@author: admin
'''

import os
import zipfile, shutil

for file_name in os.listdir():
    if ".zip" in file_name:
        filename = file_name.strip('.zip')
        with zipfile.ZipFile(file_name, 'r') as zip1:
            zip1.extractall('./'+filename)
        
        for current_file_name in os.listdir('./'+filename):
            if ".zip" in current_file_name:
                os.remove('./'+filename+'/'+current_file_name)
        
        files = os.listdir('./'+filename)
        
        for f in files:
            shutil.move('./'+filename+'/'+f, '.')
            
        with zipfile.ZipFile(file_name, 'w') as zip1:
            zip1.write('systemdetails.txt')
            zip1.write('endpointdetails.txt')
            zip1.write('triggers.txt')
            zip1.write('entitlementtypes.txt')
            zip1.write('connectionattrs.txt')
            zip1.write('connections.txt')
            zip1.write('applicationdetails.txt')
            
        
        os.remove('systemdetails.txt')
        os.remove('endpointdetails.txt')
        os.remove('triggers.txt')
        os.remove('entitlementtypes.txt')
        os.remove('connectionattrs.txt')
        os.remove('connections.txt')
        os.remove('applicationdetails.txt')        
    
        os.rmdir('./'+filename)
          
          
        
        
        