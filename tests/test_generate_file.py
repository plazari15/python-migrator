import os
import os.path

from generator import generate_migration_file


def test_generate_migration_file():
    file_name = generate_migration_file("file_test")
    return os.path.isfile(file_name)

