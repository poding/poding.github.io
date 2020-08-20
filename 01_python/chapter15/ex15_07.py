# 액세스 예제
class Date:
    def __init__(self, month):
        self.inner_month = month

    @property  # getter 함수
    def month(self):
        return self.inner_month

    @month.setter  # setter 함수
    def month(self, month):
        if 1 <= month <= 12:
            self.inner_month = month

today = Date(8)
today.month = 15

print(today.month)

# 위 아래 중에 편한 거 사용하면 됨
class Date:
    def __init__(self, month):
        self.__month = month  # __ 붙이면 프라이빗 멤버 변수

    def getmonth(self):
        return self.__month

    def setmonth(self, month):
        if 1 <= month <= 12:
            self.__month = month

    month = property(getmonth, setmonth)


today = Date(8)
today.month = 15

print(today.month)
print(today.__month)  # 외부에서 직접 접근 불가 (프라이빗 멤버 변수)

# 연산자 메소드 예제
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


kim = Human("김상형", 29)
sang = Human("김상형", 29)
moon = Human("문종민", 44)

print(kim == sang)  # True
print(kim == moon)  # False
