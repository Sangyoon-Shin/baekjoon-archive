import sys
input = sys.stdin.readline

tree = {}
total = 0
while True:
    name = input().strip()
    if not name:
        break
    total += 1
    if name not in tree:
        tree[name] = 1
    else:
        tree[name] += 1

res = sorted(tree.items())

for name, cnt in res:
    print("%s %.4f" %(name, (cnt / total)*100))
