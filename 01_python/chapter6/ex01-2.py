import random

# for x in range(1,51):
#     if(x % 10) == 0:
#         print('+', end = '')
#     else:
#         print('-',end = '')

ROCK = 0
SCISSORS = 1
PAPER = 2
com_win = 0 #컴퓨터가 이긴 횟수
com_me = 0 #내가 이긴 횟수
for num in range(3):
    com = int((random.random()*10)%3)
    me = int(input("0:바위 1:가위 2: 보"))
    print(num+1,"번 승부는")
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

