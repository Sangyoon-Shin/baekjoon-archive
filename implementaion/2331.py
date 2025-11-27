import sys
input = sys.stdin.readline

a, p = map(int, input().split())

already = set()
arr = []
already.add(a)
arr.append(a)
where = 0

while True:
    a = str(a)
    total = 0
    for i in a:
        total += int(i)**p  
    if total in already:
        where = arr.index(total)
        break
    else:
        already.add(total)
        a = total
        arr.append(total)

print(where)


    
    

