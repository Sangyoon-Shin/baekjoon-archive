n = int(input())
num = []

while n > 0:
    num.append((n % 2))
    n = n // 2

res = 0
pro = 1
for i in range(-1, -len(num) - 1, -1):
    res = res + (num[i] * pro)
    pro *= 2

print(res)
