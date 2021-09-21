import sys
import os

path = sys.argv[1]

try:
    if os.path.exists(path):
        print("File exist")
        if os.path.isfile('filepath.txt'):
            print("File exist")
        else:
            print("File not exist")
        path = open("filepath.txt", "a")
        path.write("\nBYE!")
        path.close()
except:
    sys.exit("Error code")
    print("Does not exist!")
