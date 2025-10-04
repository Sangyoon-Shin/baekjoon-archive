isbn = list(input())
total = 0
flag = 0
for i in range(len(isbn) - 1):
    if isbn[i] == '*':
        if i % 2 == 0:
            flag = 1
        else:
            flag = 3
    elif i % 2 == 0:
        total = total + int(isbn[i])
    else:
        total = total + 3 * int(isbn[i])
    
res = 0 
for num in range(10):
    if (total + flag * num + int(isbn[12])) % 10 == 0:
        res = num
        break
    
print(res)



