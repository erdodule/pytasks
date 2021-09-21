import sys
import os

path = sys.argv[1]


if os.path.exists(path):
    print("File exist!")


print ("filename : " + path.split("/")[-1])