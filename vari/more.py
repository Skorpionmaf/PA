import sys

def more(file):
    content = open(file).read().split('\n')

    while(content != [] ):
        for i in range(0,30 if len(content) > 30 else len(content)):
            print(content[0])
            del content[0]
        
        input('-----press ENTER-----')
        

if __name__ == '__main__':
    more(sys.argv[1])
