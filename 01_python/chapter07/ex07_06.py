# 1
def int_sum(*numbers):
    print(numbers)
    total = 0
    for n in numbers:
        total += n
    return total


def main():
    print(int_sum(1, 2, 3, 4, 5))
    print(int_sum())


main()

# 2
def calcstep(begin, end, step):
    total = 0
    for num in range(begin, end +1, step):
        total += num

    return total


print("3 ~ 5 =", calcstep(3, 5, 1))
print("3 ~ 5 =", calcstep(begin=3, end=5, step=1))
print("3 ~ 5 =", calcstep(step=1, end=5, begin=3))
print("3 ~ 5 =", calcstep(3, 5, step=1))
print("3 ~ 5 =", calcstep(3, step=1, end=5))

# 3
def calcstep(**args):  # 키워드 가변인수 저장방식
    # begin = args['begin']
    begin = args.get('begin', 1)  # 옵션
    end = args['end']  # 필수, 생략 불가
    # step = args['step']
    step = args.get('step', 1)  # 옵션

    total = 0
    for num in range(begin, end+1, step):
        total += num
    return total


print("3 ~ 5 =", calcstep(begin=3, end=5, step=1))
print("3 ~ 5 =", calcstep(step=1, end=5, begin=3))
print("3 ~ 5 =", calcstep(begin=1, end=5))
print("3 ~ 5 =", calcstep(end=10, step=2))


