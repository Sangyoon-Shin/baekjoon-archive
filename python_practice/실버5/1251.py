word = input()

for i in range(len(word)):
    a, b, c = map(str, word.split())
    print(a + b + c)