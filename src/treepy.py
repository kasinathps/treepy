import platform
import sys
from os import listdir,getcwd,walk
import re
OS = platform.system()
curdir = 0

#function to print all subdirectories and files in the given directory
def printdir(dir):
    dirname, subdirs, fnames = walk(dir).__next__()
    print(dirname)
    print("\n".join(subdirs))
    print("\n".join(fnames))


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

