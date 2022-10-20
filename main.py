import os
import m4
from past.builtins import execfile
from os import listdir
from os.path import isfile, join
import importlib
from colorama import Fore, Back, Style

mypath = "plugins"
intro = False
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
lengthfiles = len(onlyfiles)
quitcommand = ["exit", "quit"]

loopnumber = 0
def run_file(path):
    return exec(open(path).read());
while True:
    cmd = input("plugcmd> ")
    if cmd in quitcommand:
        exit("Quitting the shell...")
        continue
    if cmd == "textgreen":
        print(Fore.GREEN + "Text color changed to green.")
    if cmd == "textred":
        print(Fore.RED + "Text color changed to red.")
    if cmd == "textblue":
        print(Fore.BLUE + "Text color changed to blue.")
    if cmd == "textreset":
        print(Fore.GREEN + "Text color reset.")
    for i in range(0,lengthfiles):
        execfile("plugins/" + str(onlyfiles[i]))
