import sys
from itertools import permutations
input = sys.stdin.readline

n = input().strip()
digit = sorted(n, reverse=True) # 가장 큰 수 뽑는게 목적이니까 문자열을 내림차순으로 정렬해두고 숫자로 바꿔서 따지기

# 30의 배수 조건 -> 맨 뒷자리가 0, 자릿수 합이 3의 배수 -> 둘다 만족해야함
if '0' not in digit or sum(list(map(int, digit))) % 3 != 0:
    print(-1)
else:
    print(''.join(digit))

    