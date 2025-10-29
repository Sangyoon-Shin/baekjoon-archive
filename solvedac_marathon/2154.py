n = int(input())
word = ''

for i in range(1, n + 1):
    word += str(i)

print(word.index(str(n)) + 1)