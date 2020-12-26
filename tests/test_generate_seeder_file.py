import os
import os.path

from seeder_generator import generate_seeder


def test_generate_migration_file():
    file_name = generate_seeder("file_test_seeder")
    return os.path.isfile(file_name)

