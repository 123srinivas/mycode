#!/usr/bin/env pyhton3

#JSON is part of the Python Standard Library
import json

def main():

    ##create a blob of data to work with
    hitchhikers = [{"nae": "Azphod Beeblebrox", "species": "Betelgeusian"},\
     {"name": "Arthur Dent", "species": "Human"}]


## display our python data (a list containing two dictionaries)
print(hitchhikers)
##open a nes file in write mode
zfile = open("galaxyguide.json", "w")

##use the JSON library
## USAGE: json.dump(input data, file like object) ##
json.dump(hitchhikers, zfile)


##close the file when we are done
zfile.close()

main()

