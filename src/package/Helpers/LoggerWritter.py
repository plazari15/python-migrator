import sys

class Logger:

    def debug(text):
        sys.stdout.write("[DEBUG] " + str(text) + "\n")
        sys.stdout.flush()

    def info(text):
        sys.stdout.write("[INFO] " + str(text) + "\n")
        sys.stdout.flush()