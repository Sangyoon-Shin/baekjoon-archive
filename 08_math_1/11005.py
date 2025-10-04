n, b = map(int, input().split())
res = []

# A -> 65
# chr = int -> str
# ord = chr -> int

while n > 0:
    rest = n % b
    if rest < 10:
        res.append(str(rest))
    else:
        res.append(chr(rest - 10 + 65))
    n //= b

print(''.join(reversed(res)))    
