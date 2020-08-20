class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(str(self.age) + "살 " + self.name + "입니다.")


class Student(Human):
    def __init__(self, name, age, stunum):
        super().__init__(name, age)
        self.stunum = stunum

    def intro(self):  # 메서드 재정의(오버라이드), 만약 재정의 없으면 부모클래스꺼 그대로 사용
        super().intro()
        print("학번: " + str(self.stunum))

    def study(self):
        print("하늘천 따지 검을 현 누를 황")


kim = Human("김상형", 20)
kim.intro()

lee = Student("이승우", 45, 930011)
lee.intro()
lee.study()
