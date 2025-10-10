subject = input().rstrip()
cnt = 0
n = int(input())

for i in range(n):
    word = input().rstrip()
    if subject[0:5] == word[0:5]:
        cnt += 1

print(cnt)