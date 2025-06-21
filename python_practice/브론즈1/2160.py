n = int(input())
before = list(input())
after = list(input())

if(n % 2 == 1):
    flag = 0
    for i in range(len(before)):
        if(before[i] != after[i]):
            continue
        else:
            flag = 1
            break
    if(flag == 0):
        print("Deletion succeeded")
    else:
        print("Deletion failed")
elif(n % 2 == 0):
    flag = 0
    for i in range(len(before)):
        if(before[i] == after[i]):
            continue
        else:
            flag = 1
            break
    if(flag == 0):
        print("Deletion succeeded")
    else:
        print("Deletion failed")
