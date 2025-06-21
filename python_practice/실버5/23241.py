a, b = map(int, input().split())

x, y = a, b
if a > b:
    while b > 0:
        tmp = a % b
        a = b
        b = tmp
    gcd = a

else:
    while a > 0:
        tmp = b % a
        b = a
        a = tmp
    gcd = b

print((x * y) // gcd)