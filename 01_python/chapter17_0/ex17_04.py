# 클래스 데코레이터
# __붙는 메서드 : 직접 호출되지 않지만 해당 메서드가 호출되는 시점이 정해져 있음
class Outer:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print("-"*20)
        self.func()
        print("-" * 20)


@Outer  # 이거 쓰면 아래 코드 생략 가능
def inner():
    print("결과를 출력합니다.")


# inner = Outer(inner)
inner()  # 객체의 인스턴스를 함수 호출하듯이 사용했을 때 호출
