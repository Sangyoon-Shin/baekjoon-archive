arr = []

a, b = map(int, input().split())

start = 1
while True:
    if len(arr) >= 1000:
        break
    else:
        for i in range(start):
            arr.append(start)
        start += 1

sum = 0
startsum = a
for i in range(b - a + 1):
    sum = sum + arr[startsum + i - 1]

print(sum)