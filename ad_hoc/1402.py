import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print("yes")

# a < b: a * 1 * 1... 이런식으로 해버리면 a + 1 + 1 로 b를 만들어낼 수 있고
# a > b: a * (-1) * (-1) * 1... 이렇게 하면 a - 1 - 1 + 1 이니까 a - 1, 즉 a보다 작은 값도 만들어 낼 수 있다.