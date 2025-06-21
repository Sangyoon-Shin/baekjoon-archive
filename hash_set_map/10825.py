import sys
input = sys.stdin.readline

n = int(input())

score = []

for i in range(n):
    name, kor, eng, math = map(str, input().strip().split())
    k = (name, int(kor), int(eng), int(math))
    score.append(k)

score.sort(key=lambda score:(-score[1], score[2], -score[3], score[0]))

for i in score:
    print(i[0])
