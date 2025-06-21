while(1):
    n = input().strip()
    k = list(n)
    if(k[0] == '0'):
        break
    sum = len(n) + 1
    for i in k:
        if(i == '1'):
            sum += 2
        elif(i == '0'):
            sum += 4
        else:
            sum += 3
    print(sum)
    



         