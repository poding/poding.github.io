class Stack:

    def __init__(self, size=5):  # size 디폴트 값 5로 설정
        self.data = []
        self.size = size

    def push(self, data):
        if len(self.data) == self.size:  # Full 이면 리턴
            return
        self.data.append(data)

    def pop(self):
        if len(self.data) == 0:  # Empty 면 리턴
            return
        return self.data.pop()  # pop은 값 삭제 후 출력

    def clear(self):
        self.data = []

    def __str__(self):  # __붙으면 특수한 메서드
        # 관례적으로 <> 안에 주요정보 출력
        return f"<Stack size: {self.size}, data: {self.data} >"


s = Stack(10)  # size = 10
s = Stack()  # size = 5


def main():
    s1 = Stack(10)
    s1.push(10)
    s1.push(20)
    s1.push(30)
    print(s1)

    print(s1.pop())
    print(s1.pop())
    print(s1.pop())


main()
