import sys
input = sys.stdin.readline

n, m = map(int, input().split())

know = {}

for i in range(n):
    a = list(map(str, input().split()))
    if ''.join(a[2:5]) not in know.keys():
        know[''.join(a[2:5])] = a[1]
    else:
        know[''.join(a[2:5])] = 1
    
for j in range(m):
    k = list(map(str, input().split()))
    mel = ''.join(k)
    if mel in know.keys():
        if know[mel] == 1:
            print('?')
        else:
            print(know[mel])
    else:
        print('!')


