import sys
input = sys.stdin.readline

n = int(input())

res = []
buffer = []

for i in range(n):
    word = input().rstrip()
    for w in word:
        if w.isdigit():
            buffer.append(w)
        else:
            if buffer:
                res.append(int(''.join(buffer)))
                buffer = []

    if buffer:
        res.append(int(''.join(buffer)))
        buffer = []

res.sort()
for num in res:
    print(num)
        

