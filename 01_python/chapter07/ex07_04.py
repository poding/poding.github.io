def findMin(*ints):
    min = ints[0]
    for num in ints[1:]:  # 슬라이싱 사용 1번 인덱스부터 끝까지
        if num <= min:
            min = num
        print(num, end=" ")

    return min


def findMax(*ints):
    max = ints[0]
    for num in ints[1:]:
        if num >= max:
            max = num

    return max


print("최소값은???? ", findMin(2, 7, 5, -1, 20))
print("최대값은???? ", findMax(2, 7, 5, -1, 20))

print("최소값은???? ", findMin(1, 10, 6, 7, 8, 9, 7))
print("최소값은???? ", findMin(0, -6, 11, 9, 7))
lst = [2, 7, 8, 1, 0]
print("최소값은???? ", findMin(*lst))
# list = [2, 7, 5, 20]
# min = findMin(lst)
# 이렇게 호출하면 [(2, 7, 5, 20]) 리스트가 하나의 요소로 들어가기 때문에
# num > max 비교과정에서 리스트와 숫자 비교 불가라서 에러
# *붙이면 묶은 리스트를 풀어줌
# 함수 정의할 때 인자로 쓴 *는 리스트를 하나로 묶어주는 역할



