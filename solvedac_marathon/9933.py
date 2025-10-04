import sys
input = sys.stdin.readline

n = int(input())
word = {}
flag = False
for i in range(n):
    w = list(input().rstrip())
    revw = reversed(w)
    w = ''.join(w)
    revw = ''.join(revw)
    if w == revw:
        res1, res2 = len(w), w[len(w)//2]
        flag = True
    if w in word.values():
        print(len(word[revw]), word[revw][len(word[revw])//2])
        break
    else:
        word[w] = revw

if flag == True:
    print(res1, res2)