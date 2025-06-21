import sys
input = sys.stdin.readline

t = int(input())

# 맨 뒷자리만 알면 되지 않을까
# 1은 몇 제곱을하든 1
# 2는 2 4 8 16 32 64 .. -> 2 4 8 6 순서
# 3은 3 9 27 81 243... -> 3 9 7 1
# 4는 4 16 64 256... 4 6
# 5는 5 25 125... 5
# 6은 6 36 216 ... 6
# 7은 7 49 343 2401 16807... 7 9 3 1
# 8은 8 64 512 4096 32768... 8 4 2 6
# 9는 9 81 729 6561... 9 1
# 10 -> 0

for i in range(t):
    a, b = map(int, input().split())
    if a % 10 == 1:
        print(1)
    elif a % 10 == 0:
        print(0)
    elif a % 10 == 5 or a % 10 == 6:
        print(a)
    elif a % 10 == 4:
        if b % 2 == 0:
            print(6)
        else:
            print(4)
    elif a % 10 == 9:
        if b % 2 == 0:
            print(1)
        else:
            print(9)
    elif a % 10 == 2:
        ans = [6, 2, 4, 8]
        idx = b % 4
        print(ans[idx])
    elif a % 10 == 3:
        ans = [1, 3, 9, 7]
        idx = b % 4
        print(ans[idx])
    elif a % 10 == 7:
        ans = [1, 7, 9, 3]
        idx = b % 4
        print(ans[idx])
    elif a % 10 == 8:
        ans = [6, 8, 4, 2]
        idx = b % 4
        print(ans[idx])



    