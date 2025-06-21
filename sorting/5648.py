import sys
input = sys.stdin.readline

first = list(map(str, input().strip().split()))
arr = []
size = int(first[0])
firstsize = len(first)

for i in range(1, firstsize):
    arr.append(int(''.join(reversed(first[i]))))

while len(arr) < size:
    value = list(map(str, input().strip().split()))
    for i in range(len(value)):
        arr.append(int(''.join(reversed(value[i]))))

arr.sort()
for i in arr:
    print(i)





