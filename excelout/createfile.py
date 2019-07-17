#!/usr/bin/env python3
import urllib.request
import json
import webbrowser
import pyexcel

iss = 'http://api.open-notify.org/astros.json'
trackiss = urllib.request.urlopen(iss)
ztrack = trackiss.read()
result = json.loads(ztrack.decode('utf-8'))

print("\nConverted Python dat")
print(result)

list_dict = []
for item in result["people"]: 
    list_dict.append(item)
    print(item) 

pyexcel.save_as(records=list_dict, dest_file_name="ipp.xls")    
