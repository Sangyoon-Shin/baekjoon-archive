import sys
input = sys.stdin.readline

n = int(input())
code = list(input().strip())
javacode = []

for i in code:
    if i == 'J' or i == 'A' or i == 'V':
        pass
    else:
        javacode.append(i)

if len(javacode) == 0:
    print('nojava')
else:
    for k in range(len(javacode)):
        print(javacode[k], end='')