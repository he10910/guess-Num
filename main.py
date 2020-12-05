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

    minn = -1                  #定義最小值並判斷輸入是否為整數
    while minn == -1:
        minn = input("min:")
        if isint(minn) == False:
            print(error)
            minn = -1
        else:
            minn = int(minn)
            break

    maxx = -1                    #定義最大值並判斷輸入是否為整數
    while maxx == -1:
        maxx = input("max:")
        if isint(maxx) == False:
            print(error)
            maxx = -1
        else:
            maxx = int(maxx)
            break

    if maxx < minn:            #判斷最小值是否大於最大值
        print(error)
        minmax = "x"
    elif maxx - minn == 1:       #猜的範圍不包括最大及最小值本身
        print(error)
    else:
        minmax = "o"

chance = "x"                 #定義次數並判斷輸入是否為整數
while chance == "x":
    chance = input("chances:")
    if isint(chance) == False:
        print(error)
        chance = "x"
    elif int(chance) <= 0:
        print(error)
        chance = "x"
    else:
        chance = int(chance)

ans = int(random.randint(int(minn+1),int(maxx-1)))         #設定答案

gue = "x"
while gue == "x":
    if chance == 0:
        print("You have no chances.")
        print("The answer is",ans)
        break
    gue = input("range is {} to {},and you have {} chances:".format(minn,maxx,chance))
    if isint(gue) == True :
        gue = int(gue)
        if gue < ans and gue > minn:
            print("too small")
            minn = gue
            gue = "x"
            chance -=1
        elif gue > ans and gue < maxx:
            print("too big")
            maxx = gue
            gue = "x"
            chance -= 1
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