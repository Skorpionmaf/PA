import sys

def cat(file):
    print(open(file).read())

if __name__ == "__main__":
    cat(sys.argv[1])
