# 함수 데코레이터
# 함수가 실행되기 전후에 작업할 게 있을 때 사용
def inner():
    print("결과를 출력합니다.")


def outer(func):  # func 실행 전후에 ---- 를 추가
    print("-"*20)
    func()
    print("-"*20)


outer(inner)


def hello():
    print("안녕하세요")


outer(hello)

# 위에꺼를 정리하면?
def inner():
    print("결과를 출력합니다.")


def outer(func):
    def wrapper():
        print("-"*20)  # 전처리
        func()  # 기존 코드
        print("-"*20)  # 후처리
    return wrapper


inner = outer(inner)
inner()
