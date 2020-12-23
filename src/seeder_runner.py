from sys import exit, argv
from Helpers.bcolors import bcolors
import importlib.util
import os.path

seeds_file = os.listdir('seeds/')

files_to_seed = argv[1]
seed_files = None

if '--build' in files_to_seed:
    pass
elif 'run:seed' in files_to_seed:
    pass
else:
    seed_files = files_to_seed

if seed_files is None:
    seed_files = []
    print(f"{bcolors.WARNING} Nenhum Arquivo Especifico foi definido. Rodando todos os arquivos de seed. {bcolors.ENDC}")
    files = os.listdir('seeds')
    for file in files:
        if file.endswith(".py"):
            seed_files.append(file)

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
            module = importlib.util.spec_from_file_location("seeds", "seeds/" + file)
            module_from_spec = importlib.util.module_from_spec(module)
            module.loader.exec_module(module_from_spec)
            module_from_spec.run()
            print(f"{bcolors.OKGREEN} Seeded: %s {bcolors.ENDC}" % (file))
        except:
            print(f"{bcolors.WARNING} Couldn't seed: %s {bcolors.ENDC}" % (file))