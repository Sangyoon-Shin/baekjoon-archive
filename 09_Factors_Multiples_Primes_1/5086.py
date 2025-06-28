import sys
input = sys.stdin.readline

def solution(a, b):
    if a < b:
        if b % a == 0:
            print("factor")
        else:
            print("neither")
    else:
        if a % b == 0:
            print("multiple")
        else:
            print("neither")


while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    else:
        solution(a, b)

