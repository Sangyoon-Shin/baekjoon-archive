import sys

list = []
index = []

for i in range(5):
    list.append(input())

cnt = 0
for idx in range(len(list)):
    if("FBI" in list[idx]):
        index.append(idx + 1)
        cnt += 1

if(cnt == 0):
    print("HE GOT AWAY!")

print(*index)