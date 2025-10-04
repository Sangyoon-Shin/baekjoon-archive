s = input().rstrip()
target = "UCPC"
idx = 0

for ch in s:
    if ch == target[idx]:
        idx += 1
        if idx == len(target):
            break

print("I love UCPC" if idx == len(target) else "I hate UCPC")
