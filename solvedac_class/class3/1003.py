# 사이트 참고: https://dduniverse.tistory.com/entry/%EB%B0%B1%EC%A4%80-1003-DP-%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98-%ED%95%A8%EC%88%98-%ED%8C%8C%EC%9D%B4%EC%8D%AC-python
import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    # 0, 1이 호출되는 횟수만 세주면 됨
    zero = [0] * 41
    one = [0] * 41

    zero[0], one[0] = 1, 0 # fibo(0)의 경우
    zero[1], one[1] = 0, 1 # fibo(1)의 경우
    
    for j in range(2, n + 1):
        zero[j] = zero[j - 1] + zero[j - 2]
        one[j] = one[j - 1] + one[j - 2]
    print(zero[n], one[n])
