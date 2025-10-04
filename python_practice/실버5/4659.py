import sys
input = sys.stdin.readline

while True:
    word = input().strip()
    flag = 0
    mo = ['a', 'e', 'i', 'o', 'u']
    if word == 'end':
        break
    if len(word) == 1:
        if word in mo:
            flag = 1
        else:
            flag = 2
    elif len(word) == 2:
        if word[0] == word[1]:
            if word == 'ee' or word == 'oo':
                flag = 1
            else:
                flag = 2
        else:
            if word[0] in mo and word[1] in mo:
                flag = 1
            elif (word[0] in mo and word[1] not in mo) or (word[0] not in mo and word[1] in mo):
                flag = 1
            else:
                flag = 2
    else:
        for i in range(len(word) - 2):
            if word[i] in mo and word[i + 1] in mo and word[i + 2] in mo:
                flag = 2
                break
            elif word[i] not in mo and word[i + 1] not in mo and word[i + 2] not in mo:
                flag = 2
                break
            else:
                flag = 1
        if flag == 1:
            for i in range(len(word) - 1):
                if word[i] == word[i + 1]:
                    if (word[i] == 'e' and word[i] == 'e') or (word[i] == 'o' and word[i] == 'o'):
                        pass
                    else:
                        flag = 2
                        break

    if flag == 1:
        print(f"<{word}> is acceptable.")
    else:
        print(f"<{word}> is not acceptable.")
        
            

        
