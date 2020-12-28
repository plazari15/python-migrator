import os
import os.path

from migrator_function import migrate, rollback


def test_migrate():
    migrate()

def test_rollback():
    rollback()
