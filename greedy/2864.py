import sys
input = sys.stdin.readline

a, b = map(str, input().strip().split())

atmp = a.replace('5', '6')
btmp = b.replace('5', '6')
big = int(atmp) + int(btmp)

atmp = a.replace('6', '5')
btmp = b.replace('6', '5')
small = int(atmp) + int(btmp)

print(small, big)