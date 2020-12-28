from package.Helpers.bcolors import bcolors
from sys import exit, argv
import os
import shutil

def generate_seeder(filename):
    path_file = "seeds/%s.py" % (filename)

    if os.path.isfile(path_file):
        print(f"{bcolors.FAIL}Arquivo de seed já existe {bcolors.ENDC}")
        exit()

    shutil.copy("src/package/stubs/blank_seed.stub", path_file)

    return path_file


if __name__ == '__main__':
    try:
        filename = argv[1]
        print(filename, argv)
        generate_seeder(filename)
    except:
        print(f"{bcolors.FAIL}Defina um nome para o arquivo! {bcolors.ENDC}")
        exit()