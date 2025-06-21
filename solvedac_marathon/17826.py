import sys
input = sys.stdin.readline

score = list(map(int, input().split()))
score.sort(reverse=True)

n = int(input())

if n >= score[4]:
    print("A+")
elif n >= score[14]:
    print("A0")
elif n >= score[29]:
    print("B+")
elif n >= score[34]:
    print("B0")
elif n >= score[44]:
    print("C+")
elif n>= score[47]:
    print("C0")
else:
    print("F")