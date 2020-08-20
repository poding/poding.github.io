# 컬렉션 관리 함수
race = ['저그', '테란', '프로토스']
list(enumerate(race))

dates = ["월"]
food = ["갈비탕"]
price = [12000]
menu = zip(dates, food)
for d, f in menu:
    print("%s요일 메뉴 : %s" % (d, f))

# 람다 함수
# filter 예제
def flunk(s):
    return s < 60  # True/False로 리턴


def isEven(s):
    return s % 2 == 0


score = [45, 89, 72, 53, 94]
for s in filter(flunk, score):  # flunk 함수를 인자로 삼아서 전달
    print(s)

evenList = list(filter(isEven, score))
print(evenList)

# map 예제
def total(s, b):
    return s + b  # 리턴값 제한 없음


score = [45, 89, 72, 53, 94]
bonus = [2, 3, 0, 0, 5]
for s in map(total, score, bonus):
    print(s, end=", ")