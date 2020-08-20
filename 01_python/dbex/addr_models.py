#이 클래스는 기능을 제공하는 것이아니라 정보를 보관하는 클래스이다(모델클래스)
class Addr:
    def __init__(self, name, phone, addr):
        self.name = name
        self.phone = phone
        self.addr = addr

    def __str__(self):
        return f"<Addr{self.name}/{self.phone}/{self.addr}>"

    def __repr__(self):
        return f"<Addr{self.name}>"