from sys import exit, argv
from datetime import datetime
import os.path
import shutil

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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

#copy stub as class
shutil.copy("stubs/blank.stub", path_file)
#
# f = open(path_file, 'rt')
# data = f.read()
# data = data.replace("CLASS_NAME", filename)
# f.close()
#
# f = open(path_file, "wt")
# f.write(data)
# f.close()

# for line in f:
#     f.write(line.replace('CLASS_NAME', filename))

# f.close()
