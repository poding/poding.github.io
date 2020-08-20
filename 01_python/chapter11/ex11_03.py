def test(numbers):
    numbers[0] = -1  # [-1, 2, 3]으로 바뀜
    print(numbers)  # 함수 끝나면 numbers 스택 사라짐


def test2():
    numbers = [1, 2, 3]
    return numbers  # 리턴이 없을 때는 쓰레기 값


def main():
    # list1 = [1, 2, 3]
    # test(list1)  # 데이터가 아닌 참조값을 넘긴 것
    # 실질적으로 일어나는 연산은 numbers = list1

    # print(list1)

    list2 = test2()  # 참조 변수이기 때문에 쓰레기 값 X
    print(list2)


main()

# call by value : 복사본이 넘어가서 조작한 후에도 원본에 영향을 미치지 않음
# call by reference : c에서 call by address, 참조 값으로 호출해서 조작 후 원본에 영향을 미침

