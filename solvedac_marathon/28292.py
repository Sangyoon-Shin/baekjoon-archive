import sys
input = sys.stdin.readline

ant = []
start = []
start.append('1')

res = []
res.append('1')

for i in range(99):
    cur = {}
    word = []
    for num in start:
        if num not in cur:
            cur[num] = 1
        else:
            cur[num] += 1
    for key in cur.keys():
        word.append(key)
        word.append(str(cur[key]))
    start = ''.join(word)


    





