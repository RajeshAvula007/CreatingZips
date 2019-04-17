'''
Created on Feb 21, 2019

@author: admin
'''

import zipfile
import json
import os

for file_name in os.listdir():
    if ".zip" in file_name:
        
        with zipfile.ZipFile(file_name, 'r') as zip1:
            zip1.extractall() 
        
        with open('endpointdetails.txt', 'r') as txt:
            data = json.load(txt)
            data['createDate'] = ''
            data['updateDate'] = ''
        
        with open('endpointdetails.txt', 'w') as txt:
            json.dump(data, txt)
            
        with open('systemdetails.txt', 'r') as txt:
            data = json.load(txt)
            data['createDate'] = ''
            data['updateDate'] = ''
        
        with open('systemdetails.txt', 'w') as txt:
            json.dump(data, txt)
                   
        with open('entitlementtypes.txt', 'r') as txt:
            data = json.load(txt)
            data['Entitlement_types'][0]['createTaskAction'] = '0'
            for key in list(data['Entitlement_types'][0].keys()):
                if ("_label" in key) and (data['Entitlement_types'][0][key] == '') :
                    del data['Entitlement_types'][0][key]
                    
        with open('entitlementtypes.txt', 'w') as txt:
            json.dump(data, txt)
        
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
            
