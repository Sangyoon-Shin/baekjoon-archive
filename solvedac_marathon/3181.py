import sys
input = sys.stdin.readline

useless = {'i': 0, 'pa': 0, 'te': 0, 'ni': 0, 'niti': 0, 'a': 0, 'ali': 0, 'nego': 0, 'no': 0, 'ili': 0}

words = list(input().strip().split())

for i in range(len(words)):
    if i != 0 and words[i] in useless:
        pass
    else:
        print(words[i][0].upper(), end='')
