import random
import json
from os import _exit as exit

with open("setting.json" , "r" , encoding="utf-8") as jfile:
    jdata = json.load(jfile)

def isint(str):                  #判斷輸入是否為整數
    try:
        int(str)
        return True
    except ValueError:
        return False

error = jdata["Error_MSG"]
maxx = jdata["Max"]
minn = jdata["Min"]

if isint(maxx) == True:         #判斷最大值是否正確
    maxx = int(maxx)
else:
    print("錯誤的最大值")
    exit(0)

if isint(minn) == True:      #判斷最小值是否正確
    minn = int(minn)
else:
    print("錯誤的最小值")
    exit(0)

if maxx < minn:            #判斷最小值是否大於最大值
    print("最小值已經大於最大值了")
    exit(0)
elif maxx - minn == 1:       #猜的範圍不包括最大及最小值本身
    print("沒有可以猜的範圍")
    exit(0)

ans = int(random.randint(int(minn+1),int(maxx-1)))         #設定答案

gue = "x"
while gue == "x":
    gue = input("range is {} to {}:".format(minn,maxx))
    if isint(gue) == True :
        gue = int(gue)
        if gue < ans and gue > minn:
            print(jdata["Too_Small_MSG"])
            minn = gue
            gue = "x"
        elif gue > ans and gue < maxx:
            print(jdata["Too_Big_MSG"])
            maxx = gue
            gue = "x"
        elif gue not in range(minn+1,maxx):
            print(jdata["Out_Of_Range_MSG"])
            gue = "x"
        elif gue == ans:
            print(jdata["Bingo_MSG"])
            break
        else:
            print(gue)
            gue = "x"
    else:
        print(error)
        gue = "x"