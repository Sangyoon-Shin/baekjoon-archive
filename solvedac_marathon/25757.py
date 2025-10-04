import sys
input = sys.stdin.readline

n, category = map(str, input().strip().split())

name = {}
for i in range(int(n)):
    string = input().strip()
    if string in name:
        name[string] += 1
    else:
        name[string] = 1

if category == 'Y':
    print(len(name))
elif category == 'F':
    print(len(name) // 2)
else:
    print(len(name) // 3)