import os, sys
from stat import *
from datetime import datetime
from pwd import getpwuid

def getKey(item):
    return item[1]

def syntaxChange(size):
    sizes = [' B','KB','MB','TB']
    for item in sizes:
        if size < 1024:
            return "%4d%s" % (size, item)
        size = size/1024
    return size

def main():
    cwd = os.getcwd()
    if(len(sys.argv) == 1):
        for f in os.listdir(cwd):
            print(f)

    elif (len(sys.argv) == 2) and (sys.argv[1] == "-t"):
        fileList = []
        for f in os.listdir(cwd):
            fileList.append([f,os.path.getmtime(f)])
        fileList = sorted(fileList, key=getKey, reverse=True)      
        for item in fileList:
            print(item[0])

    elif (len(sys.argv) == 2) and (sys.argv[1] == "-l"):
        for f in os.listdir(cwd):
            # get last modified date
            modifiedDate = datetime.fromtimestamp(os.path.getmtime(f))
            # find owner
            owner = getpwuid(os.stat(f).st_uid).pw_name
            # find group
            group = getpwuid(os.stat(f).st_gid).pw_name
            # get file size
            size = os.stat(f).st_size
            size = syntaxChange(size)
            print(owner + " " + group + " ", end = '')
            print(size, end = '')
            print(" ",end = '')
            print(modifiedDate,end = '')
            print(" ",end = '')
            print(f)
    
if __name__ == "__main__":
    main()