# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 12:06:09 2022

@author: BET3KOR
"""
#importing regex
import re

value = []
items = [x for x in input().split(',')]

#Loop for condition check 
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A- Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
for p in items:
    if len(p)<6 and len(p)>12:
        continue
    else:
        pass
    if not re.search("([a-z])",p):
        continue
    elif not re.search("([A-Z])",p):
        continue
    elif not re.search("([0-9])",p):
        continue
    elif not re.search("([$@#])",p):
        continue
    else:
        value.append(p)
print(','.join(value))
#print(",".join(value))
# import re
# print(re.findall("[0-9]", "123"))
      