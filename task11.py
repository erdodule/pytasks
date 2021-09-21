import sys
import os
if __name__=="__main__":
    if len(sys.argv) > 1:
        p = sys.argv[1]
    else:
        p = os.path.abspath("https://github.com/erdodule/pytasks.git")

print(p)

