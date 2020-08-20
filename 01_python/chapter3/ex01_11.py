import random
x = 10
y = 20
tmp = x
x = y
y= tmp
#x와 y의 값을 교환하세요

print("x: ",x)
print("y: ",y)

# 0:rock, 1:scissors, 2:paper
com = 0
me = 1

if com==0 and me==1:print("졌습니다")
elif com==1 and me==2:print("졌습니다")
elif com==2 and me==0:print("졌습니다")
elif com==me:print("비겼습니다")
else:print("이겼습니다")

ROCK = 0
SCISSORS = 1
PAPER = 2
com = int((random.random()*10)%3)
me = int(input("0:바위 1:가위 2: 보"))
print("com",com)
if com == me:

    print("비겼습니다")
elif com == ROCK:
    if me == SCISSORS:
        print("컴퓨터가 이겼습니다")
    else:
        print("내가 이겼습니다")
elif com == SCISSORS:
    if me == ROCK:
        print("내가 이겼습니다")
    else:
        print("컴퓨터가 이겼습니다")
elif com == PAPER:
    if me == ROCK:
        print("컴퓨터가 이겼습니다")
    else:
        print("내가 이겼습니다")