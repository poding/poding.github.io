# swap 예제
def swap(x, y):
    tmp = y
    y = x
    x = tmp

    print('x', x)
    print('y', y)


a = 10
b = 20
swap(a, b)
print('a', a)
print('b', b)


# random 예제
import random
# 대문자 표기 : 상수처리, 전역변수로 공유 해도 됨
HANGMAN = """  
---+
   |
   O
  /|\\
  / \\
"""


def hangMan(lines, i):
    for line in lines[:i]:  # i 번째까지의 문자열 출력
        print(line)


def rand(start, end):
    return int(random.random()*(end-start + 1)) + start  # 범위 끝 값 포함일 때 +1
    # return number


# entry point(진입 함수, 파이썬에는 정의되어 있지 않음)
def main():

    number = rand(1, 100)
    hangManLines = HANGMAN.splitlines()  # 줄 바꿈 기준으로 분리된 리스트 생성됨
    hangManLines.pop(0)  # 처음 비어있는 문자열 제거

    for i in range(1, 6):

        num = int(input(str(i) + '번째 추측값 :'))

        if number == num:  # result = number - num if result = 0로 해도 됨
            print('정답입니다.')
            break

        else:
            if number < num:  # result > 0
                hangMan(hangManLines, i)  # hanMan 의 i번째 줄 출력
                print(num, '보다는 작습니다.')
            else:
                hangMan(hangManLines, i)
                print(num, '보다는 큽니다.')

    if number != num:  # result != 0
        print('실패했습니다. 정답은', number)


main()


