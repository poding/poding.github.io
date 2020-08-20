# 리스트 예제

def main():
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # nums = list(range(10))랑 똑같음

    print(nums[:])
    print(nums[2:5])
    print(nums[:4])
    print(nums[6:])
    print(nums[1:7:2])

    score = [88, 95, 70, 100, 99]
    print(score[2])
    score[2] = 55
    print(score[2])  # 문자열은 불변이지만 리스트는 불변 XXX

    nums = list(range(10))  # 1부터 100까지 리스트
    print(nums)

    # 리스트 대입 연산 예제
    nums2 = nums  # 데이터를 복사해서 넣는게 아니라 가리키는 것, 실제 데이터는 한개 ->참조값 (reference value)
    # C에는 포인터
    print(nums == nums2)  # 가리킨 거니까 당근 같음
    nums2[0] = -1  # 데이터가 있는 원본으로 가서 변경해서 같이 변경 됨
    print(nums)
    print(nums2)
    print(nums == nums2)

    nums = list(range(10))
    nums2 = list(range(10))
    print(nums == nums2)


main()
