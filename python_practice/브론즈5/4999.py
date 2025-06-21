import sys

speak = sys.stdin.readline()
require = sys.stdin.readline()

if(len(speak) >= len(require)):
    print("go")
else:
    print("no")