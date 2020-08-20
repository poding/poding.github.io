class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(str(self.age) + "살" + self.name + "입니다.")

    def __str__(self):  # 인스턴스 필드를 문자열로 출력
        return f"< HUMAN {self.name} ({self.age}) >"


def main():

    kim = Human("김상형", 29)
    print(kim)

    info = kim.__str__()  # __str__ 호출
    print(info)

    kim.intro()  # intro 메서드 호출

    lee = Human("이승우", 45)
    lee.intro()

    # 사용자에게 입력받아서 인스턴스 만들기
    name = input("이름 ")
    age = input("나이 ")

    h1 = Human(name, age)
    h1.intro()


main()
