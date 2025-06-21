import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    note1 = list(map(int, input().split()))
    note1dic = {}
    for k in range(n):
        if note1[k] not in note1dic.keys():
            note1dic[note1[k]] = 1

    m = int(input())
    note2 = list(map(int, input().split()))
    
    for j in note2:
        if j in note1dic.keys():
            print(1)
        else:
            print(0)
    