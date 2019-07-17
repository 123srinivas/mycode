#!/usr/bin/env python3
import re
text = "How are you doing 1,2 ,3"
a = re.search('1', text)
if a:
    print("found")
else:
    print("not found")
