import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
x = int(input())
start = 0
end = n - 1

cnt = 0
num.sort() # 정렬을 해놔야 two-pointer 쓰겠지
# 1 2 3 5 7 9 10 11 12
while start < end:
    res = num[start] + num[end]
    if res == x: # 같으면 cnt++, 두 포인터 모두 옮겨야함. 같은 수가 없으니까
        cnt += 1
        start += 1
        end -= 1
    elif res > x: # 결과가 x보다 크면, 큰 값을 작은 값으로 만들어줘야함
        end -= 1
    elif res < x:
        start += 1

print(cnt)

    
