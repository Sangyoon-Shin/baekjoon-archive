string = input().strip()

cnt0, cnt1 = 0, 0

prev = string[0]
if prev == '0':
    cnt0 += 1
else:
    cnt1 += 1

for idx in range(1, len(string)):
    if(string[idx] != prev):
        if(string[idx] == '0'):
            cnt0 += 1
        else:
            cnt1 += 1
        prev = string[idx]

print(min(cnt0, cnt1))