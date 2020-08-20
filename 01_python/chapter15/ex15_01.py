class Account:
    def __init__(self, balance):  # 생성자 함수
        self.balance = balance

    def deposit(self, money):
        self.balance += money

    def inquire(self):
        print("잔액은 %d원 입니다."%self.balance)


def main():
    account = Account(8000)  # Account의 인스턴스 생성해서 account 변수로 참조하겠다
    # class안에 함수는 메서드, 첫번째 매개변수는 파이썬이 알아서 만들어줌
    # 그래서 매개변수 개수 다름
    account.deposit(1000)
    account.inquire()


main()