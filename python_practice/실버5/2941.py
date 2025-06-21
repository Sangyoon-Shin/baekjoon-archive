import sys
input = sys.stdin.readline

string = input().strip()

cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in range(8):
    string = string.replace(cro[i], '@')

cnt = 0

for i in string:
    if i == '@':
        cnt += 1
    else:
        cnt +=1

print(cnt)
