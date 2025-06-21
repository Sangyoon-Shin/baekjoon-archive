import sys

people, extent = map(int, sys.stdin.readline().split())
report = list(map(int, sys.stdin.readline().split()))

value = extent * people

# 아래처럼 작성하면 안됨. for i in range report는 report 복사해서 가져오는거라 원본엔 영향 x.
# for i in report:
#     i = i - value

for idx in range(len(report)): # 0 ~ report - 1
    report[idx] = report[idx] - value

print(*report) # *: unpacking 연산자. 리스트 공백으로 출력