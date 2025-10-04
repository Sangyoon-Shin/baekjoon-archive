import sys
input = sys.stdin.readline

word = input().rstrip()

# 일단 java인지, c++인지, error인지 판단해야함
# "_"를 포함하고 대문자까지 있으면 error고, "_"를 포함하고 소문자로 이루어져있으면 c++, "_"가 없고 대문자가 있으면 java
speflag = False
upflag = False
downflag = False
res = []
for i in word:
    if speflag == True and upflag == True:
        print("Error!")
        break
    if i == "_":
        speflag = True
    elif i.isupper():
        upflag = True

uupflag = False
tojavaflag = False
tocplusflag = False
for w in word:
    if speflag:
        if downflag == False:
            res.append(w)
            downflag = True
        elif w == '_':
            if tojavaflag == False:
                tojavaflag = True
        elif w.islower() and tojavaflag:
            res.append(w.upper())
            tojavaflag = False
        else:
            res.append(w)
    elif upflag:
        if w.isupper():
            res.append("_")
            res.append(w.lower())
        else:
            res.append(w)

print(''.join(res))

    
    
