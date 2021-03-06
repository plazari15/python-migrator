from sys import exit, argv
from datetime import datetime
import os.path
import shutil
from package.Helpers.bcolors import bcolors

def generate_migration_file(migration_name):
    timestamp_now = datetime.now().strftime("%Y_%m_%d_%H_%M_%s")
    path_file = "migrations/%s_%s.py" % (timestamp_now, migration_name)

    if os.path.isfile(path_file):
        print(f"{bcolors.FAIL}Arquivo de migration já existe {bcolors.ENDC}")
        exit()

    shutil.copy("src/package/stubs/blank.stub", path_file)

    print(f"{bcolors.OKGREEN}%s {bcolors.ENDC}" % (path_file))

    return path_file

if __name__ == '__main__':
    try:
        filename = argv[1]
        generate_migration_file(filename)
    except Exception as e:
        print(f"{bcolors.FAIL}Defina um nome para o arquivo! {bcolors.ENDC}")
        print(str(e))
        exit()