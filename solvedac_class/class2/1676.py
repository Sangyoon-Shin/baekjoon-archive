import math

n = int(input())

factorial = []
factorial = list(str(math.factorial(n)))
strlen = len(factorial)

cnt = 0

for i in range(strlen - 1, 0, -1):
    if(factorial[i] == '0'):
        cnt += 1
    else:
        break

print(cnt)
    