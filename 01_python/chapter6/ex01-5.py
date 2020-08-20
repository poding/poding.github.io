temp=''
def kim():
    temp = "김과장의 함수"
    print(temp)
kim()
print(temp)

price = 1000

def sale():
    price = 500

sale()
print(price)


price = 1000
def sale():
    price = 500
    print("sale",id(price))

sale()
print("global",id(price))
