word = input().strip()
mo = ['a', 'e', 'i', 'o', 'u']
cnt = 0
for w in word:
    if w in mo:
        cnt += 1

print(cnt)
