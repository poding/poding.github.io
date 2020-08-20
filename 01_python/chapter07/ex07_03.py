# 지역변수 예제
# ex03_0


def kim():
    tmp = "김과장의 함수"
    print(tmp)


def lee():
    tmp = 2**10
    return tmp


def park(a):
    tmp = a*2
    print(tmp)


kim()
print(lee())
park(6)

# 전역변수 예제
# ex03_1

salerate = 0.9


def kim():
    print("오늘의 할인율:", salerate)


def lee():
    price = 1000
    print("가격:", price * salerate)


kim()
salerate = 1.1
lee()

# ex03_2
price = 1000


def sale():
    price = 500
    print(price)

sale()
print(price)

# ex03_3
price = 1000

def sale():
    price = 500
    print("sale", id(price))  # id는 주소 출력

sale()
print("global", id(price))

# global 사용 예제
# ex03_4
price = 1000

def sale():
    global price
    price = 500

sale()
print(price)

# 함수의 도움말 예제
# ex03_5
def calcsum(n):
    """합계 구해서 리턴"""  # 이 부분에 적은 설명을 출력해줌
    total = 0
    for i in range(n+1):
        total += i

    return total

help(calcsum)