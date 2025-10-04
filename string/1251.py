word = input().rstrip()

n = len(word)
res = []

for i in range(1, n):
    for j in range(i + 1, n):
        part1 = word[:i][::-1] # 파이썬 문법으로 [start, stop, step]인데, step에 -1 넣으면 뒤집힌다.
        part2 = word[i:j][::-1]
        part3 = word[j:][::-1]
        res.append(part1 + part2 + part3)

print(min(res))
