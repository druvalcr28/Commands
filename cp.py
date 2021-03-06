import os, sys
from stat import *

def main():
    last_argument = sys.argv[len(sys.argv)-1]
    mode = os.stat(last_argument)[ST_MODE]

    if (len(sys.argv) < 3):
        if (len(sys.argv) == 1):
            print("Enter source file/files")
        print("Enter a destination file or directory")
        sys.exit()

    elif S_ISDIR(mode) and (sys.argv[1] != "-R"):   #OPTIMIZE IT
        for f in sys.argv[1:len(sys.argv)-1]:
            src_file = open(f,"r")
            pathname = os.path.join(last_argument,f)
            dest_file = open(pathname,"w+")
            copyfile(src_file,dest_file)

    elif S_ISREG(mode) and (len(sys.argv) == 3):
        src_file = open(sys.argv[1],"r")
        dest_file = open(sys.argv[2],"w+")
        for line in src_file:
            copyfile(src_file,dest_file)

    elif (sys.argv[1] == "-R") and (S_ISDIR(os.stat(sys.argv[2])[ST_MODE])):    #ASSUMING THAT DEST IS ALREADY A DIR 
        os.mkdir(os.path.join(sys.argv[3],sys.argv[2]))
        copydir(sys.argv[2],os.path.join(sys.argv[3],sys.argv[2]))
    
    else:
        print("cannot execute command")
        sys.exit()  

def copydir(src_dir,dest_dir):
    for f in os.listdir(src_dir):
        pathname = os.path.join(src_dir,f)
        mode = os.stat(pathname)[ST_MODE]

        if S_ISDIR(mode):
            os.mkdir(os.path.join(dest_dir,f))
            copydir(pathname,os.path.join(dest_dir,f))
        elif S_ISREG(mode):
            src_file = open(pathname,"r")
            pn = os.path.join(dest_dir,f)
            dest_file = open(pn,"w+")
            copyfile(src_file,dest_file)
        else:
            print("cannot execute command")
            sys.exit()

def copyfile(src_file,dest_file):
    for line in src_file:
        dest_file.write(line)

if __name__ == "__main__":
    main()