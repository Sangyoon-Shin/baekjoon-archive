word = ['M', 'O', 'B', 'I', 'S']
n = input().rstrip()

flag = True
for i in word:
    if i in n:
        pass
    else:
        flag = False

if flag:
    print("YES")
else:
    print("NO")



