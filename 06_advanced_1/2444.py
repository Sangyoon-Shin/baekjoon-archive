n = int(input())

for i in range(1, n + 1):
    print(" " * (n - i), end='')
    print("*" * (2 * i - 1), end='')
    # print(" " * (n - i),end='')
    print()

for i in range(1, n):
    print(" " * i, end='')
    print("*" * (2 * (n - i) - 1), end='')
    # print(" " * i, end='')
    print()
