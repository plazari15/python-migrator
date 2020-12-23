from sys import exit, argv
from datetime import datetime
import os.path
import shutil
from bcolors import bcolors

try:
    filename = argv[1]
except:
    print(f"{bcolors.FAIL}Defina um nome para o arquivo! {bcolors.ENDC}")
    exit()

timestamp_now = datetime.now().strftime("%Y_%m_%d_%H_%M_%s")
path_file = "migrations/%s_%s.py" % (timestamp_now, filename)

if os.path.isfile(path_file):
    print(f"{bcolors.FAIL}Arquivo de migration já existe {bcolors.ENDC}")
    exit()

shutil.copy("stubs/blank.stub", path_file)
