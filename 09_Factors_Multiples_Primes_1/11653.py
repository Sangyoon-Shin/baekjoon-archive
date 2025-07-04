import sys
input = sys.stdin.readline

def solution(n):
    flag = 0
    if n == 1:
        pass
    else:
        while True:
            if flag == 1:
                break
            for i in range(2, n + 1):
                if n % i == 0 and n // i != 1:
                    n = n // i
                    print(i)
                    break
                elif n % i == 0 and n // i == 1:
                    flag = 1
                    print(i)
                    break
    
n = int(input())
solution(n)