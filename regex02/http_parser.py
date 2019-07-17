#!/usr/bin/env python3
import urllib.request
import re

url = input("Where should we search (url)?  ")
print("Great! So we'll try to open this url " + 'https://alta3.com' + " to search for the phrase:")
searchFor = input()
searchMe = urllib.request.urlopen("https://alta3.com").read().decode("utf-8")
if re.search(searchFor, searchMe):
    print("Found a match!")
else:
    print("No match!")
