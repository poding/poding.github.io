# ex02_0
def intsum(*ints):
    total = 0
    for num in ints:
        total += num

    return total


print(intsum(1, 2, 3))
print(intsum(5, 6, 7, 9, 11, 13))
print(intsum(8, 9, 6, 2, 9, 7, 5, 8))

# ex02_1
# 기본값 배정은 뒤에서부터 해야 됨 중간에 건너뛸 수 없음


def calcstep(begin, end, step = 1):
    total = 0
    for num in range(begin, end+1, step):
        total += num

    return total


print("1 ~ 10 =", calcstep(1, 10, 2))
print("2 ~ 10 =", calcstep(1, 100))  # 세번째 인수 입력 안하면 기본 값으로 설정


# ex02_2
def kim():
    temp = "김과장의 함수"
    print(temp)


kim()
# print(temp)는 사용 X 지역변수는 함수 안에서만 호출 가능
