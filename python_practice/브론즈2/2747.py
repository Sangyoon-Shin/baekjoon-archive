# 메모이제이션. 이전에 나왔던거 기록해두고 있으면 그 값 뽑아 출력, 없으면 추가
memoization = {}

def fibo(n):
    if n in memoization:
        return memoization[n]
    if n <= 1:
        memoization[n] = n
    else:
        memoization[n] = fibo(n - 1) + fibo(n - 2)
    return memoization[n]

n = int(input())
print(fibo(n))