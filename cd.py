#https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory
#os.chdir(path)
#
import os, sys
from stat import *

def reverse(path):
    s = ""
    for i in path:
        s = s + i
    return s    

def pathUptoStar(path):
    tmp = path.split('/')[-1]
    


def stringUptoStar(path):
    result = ""
    i = 0
    while (path[i] !== "*"):
        result = result + path[i]
        i = i+1
    return result    

def main():
    if (len(sys.argv) == 1):
        os.chdir("/")
        os.system("/bin/bash")
    elif (len(sys.argv) == 2):
        path = sys.argv[1]
        if (path.find("*")):
            full_path = stringUptoStar(path)
            full_path = pathUptoStar(full_path)      

        elif (path[0] === "~") and (len(path) == 1):
            os.chdir("/")
            os.system("/bin/bash")
        else:    
            path = sys.argv[1]
            os.chdir(path)
            os.system("/bin/bash")



if __name__ == "__main__":
    main()