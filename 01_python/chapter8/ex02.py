s="python"
for c in s:
    print(c,end = ",")

s = "python"
for i in range(len(s)):
    print(s[i],end=",")

print()

s = "python programming"
print(len(s))
print(s.find('o'))
print(s.rfind('o'))
print(s.index('r'))
print(s.count('n'))

name = "홍길동"

if name.startswith("홍"):
    print("홍씨입니다.")
if name.startswith("김"):
    print("김씨입니다")
file = "figure.jpg"
if file.endswith(".jpg"):
    print("jpg 그림 파일입니다")


s="Hello"
print(s[2])

s="Good morning. my love KIM"

print(s.lower())
print(s.upper())
print(s.swapcase())
print(s.capitalize())
print(s.title())

s="독도는 일본땅. 대마도도 일본땅"
print(s)
print(s.replace("일본" , "한국"))
print(s)

message = "안녕하세요"
print(message.center(30))
print(message.ljust(30))
print(message.rjust(30))

price = 500
print("궁금하면 "+str(price)+ "원!")

price = [30,13500,2000]
for p in price:
    print("가격 : %d원"%p)
print()
for p in price:
    print("가격 : %")


name="한결"
age=16
height=162.5
print("이름:{}, 나이:{}, 키:{}".format(name,age,height))
print("이름:{:s}, 나이:{:d},키:{:f}".format(name,age,height))
print("이름:{:4s}, 나이:{:3d},키:{:.2f}".format(name,age,height))

print("이름:{0}, 나이: {1}, 키: {2}".format(name,age,height))
print("이름:{2}, 나이: {1}, 키: {0}".format(height,age,name))
print("이름:{name}, 나이: {age}, 키: {height}".format(age=20,height=160.9,name="길동"))

print(f"이름:{name}, 나이: {age}, 키: {height:.2f}")

