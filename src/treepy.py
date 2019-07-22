import platform
import sys
from os import listdir,getcwd,walk
import re
OS = platform.system()
def Windows(arg):
    print(f"{arg}\n|-->", end = "")
    print("\n|-->".join(listdir(str(arg))))

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

def printdir(dir):
    for dirname, subdirs, fnames in os.walk(dir):
        