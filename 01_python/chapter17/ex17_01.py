def makeHello(message):
    def hello(name):
        print(message+","+name)
    return hello

enghello = makeHello("Good Morning")
kohello = makeHello("안녕하세요")

enghello("Mr Kim")
kohello("홍길동")



def outer(func):
    print("-"*20)
    func()
    print("-"*20)
@outer
def inner():
    print("결과를 출력합니다.")
    
inner()

