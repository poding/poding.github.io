# 함수 예제
# ex01_0
def calcsum(n):
    total = 0
    for num in range(n+1):
        total += num

    return total


print("~4 =", calcsum(4))
print("~10 =", calcsum(10))

# ex01_1
def calcrange(begin, end):
    total = 0
    for num in range(begin, end+1):
        total += num

    return total


print("3 ~ 7 =", calcrange(3, 7))

# ex01_2
def printsum(n):
    total = 0
    for num in range(n+1):
        total += num
    print("~", n, "=", total)


printsum(4)
printsum(10)

