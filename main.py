import random

error = "error,try again!"

def isint(str):                  #判斷輸入是否為整數
    try:
        int(str)
        return True
    except ValueError:
        return False
    
minmax = "x"
while minmax == "x":

    maxx = -1                    #定義最大值並判斷輸入是否為整數
    while maxx == -1:
        maxx = input("max:")
        if isint(maxx) == False:
            print(error)
            maxx = -1
        else:
            maxx = int(maxx)
            break

    minn = -1                  #定義最小值並判斷輸入是否為整數
    while minn == -1:
        minn = input("min:")
        if isint(minn) == False:
            print(error)
            minn = -1
        else:
            minn = int(minn)
            break
    
    if maxx < minn:            #判斷最小值是否大於最大值
        print(error)
        minmax = "x"
    elif maxx - minn == 1:       #猜的範圍不包括最大及最小值本身
        print(error)
    else:
        minmax = "o"

ans = int(random.randint(int(minn+1),int(maxx-1)))         #設定答案

gue = "x"
while gue == "x":
    gue = input("range is {} to {}:".format(minn,maxx))
    if isint(gue) == True :
        gue = int(gue)
        if gue < ans and gue > minn:
            print("too small")
            minn = gue
            gue = "x"
        elif gue > ans and gue < maxx:
            print("too big")
            maxx = gue
            gue = "x"
        elif gue not in range(minn+1,maxx):
            print("out of range,try again!")
            gue = "x"
        elif gue == ans:
            print("bingo!")
            break
        else:
            print(gue)
            gue = "x"
    else:
        print(error)
        gue = "x"