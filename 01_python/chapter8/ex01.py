import random

def rand(start, end):
    return int(random.random()*(end-start+1)) + start
    #return number

# def main():
#     start = 1
#     end = 6
#     number = rand(start, end)
#     print(number)
#
# main()

def main():
    number = rand(1,100)

    for i in range(1,6):
        num = int(input(str(i)+"번째 추측값: "))
        result = number -num
        if result ==0:
            print("정답입니다.")
            break
        elif result > 0:
            print(num,"보다는 큽니다.")
        else:
            print(num,"보다는 작습니다.")
    if result != 0:
        print('실패했습니다.\n정답은 ',number)








    # answer = False
    # cnt=1
    # number = rand(start, end)
    # print(number)
    # while answer==False:
    #     print(cnt,end="")
    #     num = int(input("번째 추측값:"))
    #     if cnt == 5:
    #         answer = True
    #         print("실패했습니다")
    #     elif number == num:
    #         print("정답입니다")
    #         answer = True
    #     elif number > num:
    #         print(num,"보다는 큽니다")
    #         cnt+=1
    #     elif number < num:
    #         print(num,"보다는 작습니다")
    #         cnt+=1

main()


