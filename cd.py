import os, sys
from stat import *
from os.path import expanduser

def main():
    if (len(sys.argv) == 1):
        os.chdir("/")
        os.system("/bin/bash")
    elif (len(sys.argv) == 2):
        path = sys.argv[1]
        if (path[0] == "~") and (len(path) == 1):
            home = expanduser("~")
            os.chdir(home)
            os.system("/bin/bash")
        else:    
            path = sys.argv[1]
            try:
                os.chdir(path)
            except OSError:
                print("No such directory: '%s'" % path)
                sys.exit()
            os.system("/bin/bash")
    else:
        print("error occured")


if __name__ == "__main__":
    main()