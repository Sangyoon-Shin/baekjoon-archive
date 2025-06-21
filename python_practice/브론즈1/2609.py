a, b = map(int, input().split())

a_ = max(a, b)
b_ = min(a, b)

while(a_ % b_ != 0):
    r = a_ % b_
    a_ = b_
    b_ = r

gcd = b_
lcd = (a * b) // gcd

print(gcd)
print(lcd)