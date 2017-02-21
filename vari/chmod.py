import os, sys

def chmod(file, mode):
    os.chmod(file, int(mode, base=8))

if __name__ == "__main__":
    chmod(sys.argv[2], sys.argv[1])
