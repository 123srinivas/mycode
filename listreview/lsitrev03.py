#!/usr/bin/env python3

def main():
    ## create a lsit already containing IP addreses (strings)
    iplist = [['10.0.0.1', '10.0.1.', '10.3.2.1']

    ##create  al ist of ports (strings)
    iplist2 = ''5060', '80', '22']

    ##display list
    print(iplist)

    ##UASE TE EXTEND METHOD ON IPLIST, OUR LIST OBJECT
    ## Extend iterates over each 'thing' it is passed, and adds them to a list object
    iplist.extend(iplist2)
    ## show how iplist has changed
    print(iplist)
    main():
