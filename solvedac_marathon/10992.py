n = int(input())
if n == 1:
    print('*')
else:
    for i in range(n - 1):
        if i == 0:
            print(" " * (n - 1), end='')
            print("*")
        else:
            print(" " * (n - i - 1), end='')
            print("*",end='')
            print(" " * (2*i - 1),end='')
            print("*")
    print("*"*(2*n - 1))

