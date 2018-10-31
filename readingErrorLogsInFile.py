# python 3.6
# This program will print line(s) which contains error log

import os
import re

myFile = 'F:\\My Python Scripts\\error.txt'

def RegEx(file):
    openFile = open(myFile, 'r') 
    myResList = []
    myList = openFile.readlines()
    myReg = re.compile(r'error')
    for i in (myList):
            result = myReg.search(i)
            if result != None:
                    myResList.append(i)
    final = '\n'.join(myResList)
    return final

print()
print('Results:')
print(RegEx(myFile))
print()

