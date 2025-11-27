import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    wow = input().strip()
    cnt = 0
    for j in range(len(wow) - 2):
        if wow[j:j+3] == "WOW":
            cnt += 1
    print(cnt)

    





        