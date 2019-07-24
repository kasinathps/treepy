import platform
import sys
from os import listdir,getcwd,walk
import re
OS = platform.system()
curdir = 0

#function to print all subdirectories and files in the given directory
def printdir(dir):
    dirname, subdirs, fnames = walk(dir).__next__()
    print(f"\n{str(dirname)}\tSubdirs : {str(len(subdirs))}\tFiles : {str(len(fnames))}\n")
    printsubdirs(subdirs,dirname)
    print("\n".join(fnames))

def printsubdirs(subdirs,dirname):
    for i in subdirs:
        a,b,c = walk(f"{dirname}\\{str(i)}").__next__()
        print("{: <20}Subdirs : {: <20}Files : {: <20}".format(str(i),len(b),len(c)))



def Windows(arg):
    printdir(arg)
    curdir = 0

def Linux():
    pass

def Macos():
    pass

os_f = {
    "Windows": Windows,
    "Darwin": Macos,
    "Linux": Linux,
}
def main(arg = sys.argv):
    if len(arg) == 1:
        os_f[OS](getcwd())
    else :
        os_f[OS](arg[1])
    return 0

if __name__ == "__main__":
    main()

