arr = set()

for i in range(10000):
    value = str(i)
    sum = i
    for j in range(len(value)):
        sum = sum + int(value[j])
    arr.add(sum)

for i in range(10000):
    if i not in arr:
        print(i)
