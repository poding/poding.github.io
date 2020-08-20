# 제너레이터
# 열거 가능 객체가 귀찮아서 대체
# return 과 차이? return 은 루프 돌고 리턴되면 바로 끝남


def seqgen(data):  # __next()__ 에 해당되는 내용
    for index in range(0, len(data), 2):
        yield data[index:index+2]  # yield 는 루프 돌면서 계속 리턴


solarterm = seqgen("입춘우수경칩춘분청명곡우입하소만망종하지소서대서")  # 형태적으로는 함수와 같음
print(solarterm)  # 출력해보면 함수 실행되는게 아니라 객체로 변환시키겠다는 의미

for k in solarterm:
    print(k, end=',')


# 일급시민
# 함수를 값처럼 쓸 수 있느냐의 여부 (변수와 동일한 특성을 가짐)

#01
def add(a, b):
    print(a + b)


plus = add

plus(1, 2)

#02
def calc(op, a, b):  # 함수의 인자로 함수를 전달
    op(a, b)


def add(a, b):
    print(a + b)


def multi(a, b):
    print(a * b)


calc(add, 1, 2)
calc(multi, 3, 4)


# 지역함수 (함수 안에 함수를 정의해서 사용)
# 이름 충돌 방지하기 위해서 사용(이름 충돌 시 앞에 정의된 함수 사용불가)

#1
def calcsum(n):
    def add(a, b):  # 지역함수 calcsum() 내에서만 호출 가능
        return a + b

    total = 0
    for i in range(n+1):
        total = add(total, i)

    return total


print("~ 10 = ", calcsum(10))

#2 (가볍게 보고 넘어가기)
def makeHello(message):
    def hello(name):  # closure 함수
        print(message + ", " + name)
    return hello


enghello = makeHello("Good Morning")
kohello = makeHello("안녕하세요")

enghello("Mr Kim")
kohello("홍길동")
