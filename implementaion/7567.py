import sys
input = sys.stdin.readline

plate = input().rstrip()

cur = plate[0]
total = 10

for i in range(1, len(plate)):
    if cur == plate[i]:
        total += 5
    else:
        cur = plate[i]
        total += 10

print(total)
    