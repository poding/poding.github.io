# 클래스 메소드 예제
class Car:
    count = 0  # 공유값, 인스턴스랑 무관해서 self. 안하고 Car.count

    def __init__(self, name):
        self.name = name
        Car.count += 1

    @classmethod  # 인스턴스에 대한 정보 X(self 가 넘어오지 않음), 클래스의 참조 cls 가 넘어옴
    def outcount(cls):
        print(cls.count)


pride = Car("프라이드")
korando = Car("코란도")
Car.outcount()

# 정적 메소드 예제
class Car:
    @staticmethod
    def hello():
        print("오늘도 안전 운행 합시다.")

    count = 0

    def __init__(self, name):
        self.name = name
        Car.count += 1

    @classmethod
    def outcount(cls):
        print(cls.count)


Car.hello()
