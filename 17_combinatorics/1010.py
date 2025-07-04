import math

n = int(input())

def nCr(b, a):
    # nPr = n!/(n-r)!
    # nCr = n!/r!(n-r)!
    res = math.factorial(a) / (math.factorial(b) * math.factorial(a - b))
    print(int(res))

    # math.comb(n, r) = nCr 
    # factorial => O(n)
    # from itertools import combinations => 모든 조합 데이터 생성하기에 시간초과

for i in range(n):
    west, east = map(int, input().split())
    nCr(west, east)