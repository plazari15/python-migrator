from sys import exit, argv
from package.Helpers.bcolors import bcolors
import importlib.util
import os.path
from package.Seeder.Seeder import Seeder
import shutil

import multiprocessing

def run_seed_function(file):
    module = importlib.util.spec_from_file_location("seeds", "seeds/" + file)
    module_from_spec = importlib.util.module_from_spec(module)
    module.loader.exec_module(module_from_spec)
    module_from_spec.run()

def get_seeds():
    seeder = Seeder()

    module = importlib.util.spec_from_file_location("seeds", "seeds/database_seeder.py")
    module_from_spec = importlib.util.module_from_spec(module)
    module.loader.exec_module(module_from_spec)
    module_from_spec.define(seeder)

    return seeder.get_list()


def run_seeders():
    queue = multiprocessing.Queue(-1)
    seed_files = None
    try:
        files_to_seed = argv[1]
    except:
        files_to_seed = os.listdir('seeds/')

    if '--build' in files_to_seed:
        pass
    elif 'run:seed' in files_to_seed:
        pass
    else:
        seed_files = files_to_seed

    if seed_files is None:
        seed_files = []
        print(f"{bcolors.WARNING} Nenhum Arquivo Especifico foi definido. Rodando todas as seeds declaradas em seeds/database_seeder.py. {bcolors.ENDC}")
        if os.path.isfile("seeds/database_seeder.py"):
            seed_files = get_seeds()
        else:
            shutil.copy("src/package/stubs/database_seeder.stub", "seeds/database_seeder.py")
            print(
                f"{bcolors.WARNING} arquivo criado seeds/database_seeder.py. Antes de Continuar, declare as Seeds que deseja rodar. {bcolors.ENDC}")

    if seed_files is None:
        print(f"{bcolors.FAIL} Nenhum Arquivo Especifico foi definido. Erro{bcolors.ENDC}")
        exit()

    if len(seed_files) == 0:
        print(f"{bcolors.FAIL} Nenhum arquivo de Seed encontrado {bcolors.ENDC}")
        exit()

    if len(seed_files) > 0:
        for file in seed_files:
            try:
                file = file if file.endswith(".py") else file + ".py"
                worker = multiprocessing.Process(target=run_seed_function, args=(file,))
                worker.start() #Starta o processo
                worker.join() #Segura o for até a conclusão do SubProcesso.
                print(f"{bcolors.OKGREEN} Seeded: %s {bcolors.ENDC}" % (file))
            except Exception as e:
                print(f"{bcolors.WARNING} Couldn't seed: %s {bcolors.ENDC}" % (file))
                print(str(e))


if __name__ == '__main__':
    run_seeders()