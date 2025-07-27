import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    word = list(input().strip())
    finda, findb = 0, 0
    while len(word) != 0:
        k = word.pop()
        if k == 'A' and finda == 0:
            finda = 1
        





