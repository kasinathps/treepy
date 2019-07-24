import platform
import sys
from os import listdir,getcwd,walk
import re
OS = platform.system()
curdir = 0

#function to print all subdirectories and files in the given directory
def printdir(dir):
    for (dirname, subdirs, fnames) in walk(dir):
        print(dirname)
        print("\n".join(subdirs))
        print("\n".join(fnames))
        subdirs[:] = []


def Windows(arg):
    printdir(arg)

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

