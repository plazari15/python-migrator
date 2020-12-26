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

def generate_migration_file(migration_name):
    timestamp_now = datetime.now().strftime("%Y_%m_%d_%H_%M_%s")
    path_file = "migrations/%s_%s.py" % (timestamp_now, migration_name)

    if os.path.isfile(path_file):
        print(f"{bcolors.FAIL}Arquivo de migration já existe {bcolors.ENDC}")
        exit()

    shutil.copy("src/stubs/blank.stub", path_file)

    return path_file

if __name__ == '__main__':
    try:
        filename = argv[1]
        generate_migration_file(filename)
    except:
        print(f"{bcolors.FAIL}Defina um nome para o arquivo! {bcolors.ENDC}")
        exit()