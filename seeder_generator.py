from bcolors import bcolors
from sys import exit, argv
import os
import shutil

try:
    filename = argv[1]
except:
    print(f"{bcolors.FAIL}Defina um nome para o arquivo! {bcolors.ENDC}")
    exit()

path_file = "seeds/%s.py" % (filename)

if os.path.isfile(path_file):
    print(f"{bcolors.FAIL}Arquivo de seed já existe {bcolors.ENDC}")
    exit()

shutil.copy("stubs/blank_seed.stub", path_file)

