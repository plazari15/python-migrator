#busca os arquivos na pasta migrations
    #Arquivos são escritos com 2 funções python
    #Executa no MongoDB

from sys import exit, argv
import os.path
import importlib.util

from datetime import datetime
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

#Verifica se usuário passou a ação
try:
    action = argv[1] #migrate, rollback
    method = 'up' if action == 'migrate' else 'down'
except:
    print(f"{bcolors.FAIL}Defina uma action antes de mais nada! {bcolors.ENDC}")
    exit()

#Lista arquivos no diretorio
files = os.listdir('migrations')

#Percorre cada arquivo do diretório
for file in files:
    if file in ['__pycache__']:
        continue

    module = importlib.util.spec_from_file_location("migrations", "migrations/"+file)
    module_from_spec = importlib.util.module_from_spec(module)
    module.loader.exec_module(module_from_spec)

    if action == 'migrate':
        module_from_spec.up()
    elif action == 'rollback':
        module_from_spec.down()
    else:
        print(f"{bcolors.FAIL}Esta aplicação não suporta isso! {bcolors.ENDC}")
        exit()