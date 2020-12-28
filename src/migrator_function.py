from sys import exit, argv
import os.path
import importlib.util
from package.Helpers.bcolors import bcolors
from database_migration_repository import create_migration_register, get_files_from_last_batch, \
    delete_migration_register, get_batch_id, check_file


def migrate():
    batch_id = get_batch_id()

    # Lista arquivos no diretorio
    files = os.listdir('migrations')
    if len(files) > 0:
        for file in files:
            if file.endswith(".py"):
                file_name = file.replace(".py", "")

                module = importlib.util.spec_from_file_location("migrations", "migrations/" + file)
                module_from_spec = importlib.util.module_from_spec(module)
                module.loader.exec_module(module_from_spec)

                try:
                    if check_file(file_name):
                        print(f"{bcolors.WARNING}Migrating: %s {bcolors.ENDC}" % file_name)
                        module_from_spec.up()
                        create_migration_register(file_name, batch_id)
                        print(f"{bcolors.OKGREEN}Migrated: %s {bcolors.ENDC}" % file_name)
                except Exception as e:
                    print(f"{bcolors.FAIL} Erro: %s! {bcolors.ENDC}" % (str(e)))
                    exit()
    else:
        print(f"{bcolors.WARNING} %s! {bcolors.ENDC}" % ("Nothing to Migrate"))
        exit()


def rollback():
    get_file_from_last_batch = get_files_from_last_batch()
    if get_file_from_last_batch is not False:
        for file in get_file_from_last_batch['files']:
            try:
                print(f"{bcolors.WARNING}Rolling back: %s {bcolors.ENDC}" % file)
                module = importlib.util.spec_from_file_location("migrations", "migrations/" + file + ".py")
                module_from_spec = importlib.util.module_from_spec(module)
                module.loader.exec_module(module_from_spec)

                module_from_spec.down()
                print(f"{bcolors.OKGREEN}Rolled back: %s {bcolors.ENDC}" % file)
            except Exception as e:
                print(f"{bcolors.FAIL} Erro: %s! {bcolors.ENDC}" % (str(e)))
                exit()

        delete_migration_register(get_file_from_last_batch['_id'])
    else:
        print(f"{bcolors.WARNING} %s! {bcolors.ENDC}" % ("Nothing to Rollback"))
        exit()


if __name__ == '__main__':
    try:
        action = argv[1]  # migrate, rollback
        if action == 'migrate':
            migrate()
        elif action == 'rollback':
            rollback()

    except Exception as e:
        print(f"{bcolors.FAIL}Defina uma action antes de mais nada! {bcolors.ENDC}")
        raise e
        exit()
