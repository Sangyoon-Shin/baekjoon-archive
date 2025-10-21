n = input().strip()
f = int(input())

i = 0
n = list(n)
n[-1] = '0'
n[-2] = '0'
n = int(''.join(n))

while True:
    if (n + i) % f == 0:
        n = str(n + i)
        print(n[-2:])
        break
    else:
        i += 1