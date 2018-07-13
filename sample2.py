import os, sys
from stat import *

def reverse(path):
    s = ""
    for i in path:
        s = i + s
    return s

def getNextdir(fullS):
    nextDir = fullS.split("/")[-1]
    for f in os.listdir():

def filterFullpath(fullS):
    i = len(fullS)-1
    while (i > -1):
        if (fullS[i] == "/"):
            return fullS[:i+1]
        i = i-1
    return None   

def getRestPath(givenP,fullS):
    fullS = fullS + "*"
    result = givenP.split(fullS)[1]
    return result

def stringUptoStar(path):
    result = ""
    i = 0
    while (path[i] != "*"):
        result = result + path[i]
        i = i+1
    return result

def main():
    givenPath = "/media/abc/def/dp*/jmt/li*"
    fullstring = stringUptoStar(givenPath)
    givenPath = getRestPath(givenPath,fullstring)
    fullPath = filterFullpath(fullstring)
    fullPath = getNextdir(fullstring)



if __name__ == "__main__":
    main()