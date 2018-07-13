import os, sys
from stat import *

def checkSyntax(directory,msg):
    if (directory[0] == "/") or (directory[0] == "~"):
        if(directory[len(directory)-1] == "/"):
            directory = directory[:len(directory)-1]
        fullPath = findPath(directory)
        print(fullPath)
        try:
            if(os.path.isdir(fullPath[1])):
                os.chdir(fullPath[1])
                makeDir(fullPath[0],1)
        except:
            print("error occured")
            sys.exit()
    else:
        makeDir(directory,msg)

def findPath(directory):
    last_dir = directory.split('/')[-1]
    result = [last_dir]
    i = len(directory)-1
    while(i > -1):
        if(directory[i] == "/"):
            result.append(directory[:i+1])
            return result
        i = i-1
    result.append("/")    
    return result

def makeDir(directory,msg):
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
            if(msg):
                print("mkdir: created directory '%s'" % directory)
        except OSError:
            print("error-occured")
            sys.exit()
    else:
        print("mkdir: cannot create directory '%s': File exists" % directory)         

def main():
    pwd = os.getcwd()

    if(sys.argv[1] == "-v"):
        for directory in sys.argv[2:]:
            checkSyntax(directory,1)
    else:
        for directory in sys.argv[1:]:
            checkSyntax(directory,0)
            
    print("eva")


if __name__ == "__main__":
    main()