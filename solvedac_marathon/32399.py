n = list(input().strip())

if n[0] == '1':
    print(1)
elif n[1] == '1':
    if n[2] == ')':
        print(0)
    else:
        print(2)
else:
    print(1)
    