import sys
input = sys.stdin.readline

n = int(input())
while True:
    if n == 0:
        break
    else:
        words = []
        for i in range(n):
            word = input()
            words.append(word)
        sorted_words = sorted(words, reverse=True)
        print(sorted_words[0],end='')
        n = int(input())
