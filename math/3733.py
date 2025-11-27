import sys
input = sys.stdin.readline

while True:
    line = input().strip()
    if not line:  
        break
    n, x = map(int, line.split())
    print(x // (n + 1))
