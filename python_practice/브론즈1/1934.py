# 유클리드 호제법
# a > b 일때, a를 b로 나눈 나머지 r 값이 0이 될 때 까지 a = a % b, b = r로 초기화. 마지막에 r = 0 으로 만들도록 나누는 수가 최대공약수
# (a * b) // r =
n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    a_ = max(a, b)
    b_ = min(a, b)

    while((a_ % b_) != 0):
        r = a_ % b_
        a_ = b_
        b_ = r
    gcd = b_
    lcm = (a * b) // gcd
    
    print(lcm)
    
# import math

# n = int(input())
# for i in range(n):
#     a, b = map(int, input().split())
#     print((a * b) // math.gcd(a, b))
