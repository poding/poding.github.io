# 리스트 예제
def main():
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    nums[2:5] = [20, 30, 40]
    print(nums)
    nums[6:8] = [60, 70, 80, 90]  # 갯수가 안맞을 땐 기존에 있던거 먼저 두개 삭제되고 새로운 값 대체
    print(nums)
    nums[6:6] = [100, 200]  # 기존값 삭제 하지 않으면서 추가하기, 리스트 크기가 늘어남
    print(nums)
    nums[6:8] = [60]
    print(nums)


main()
# 문자열은 불변이라서 이렇게 대입 연산이 안됨(읽기는 되지만 쓰기는 안됨)


list1 = [1, 2, 3, 4, 5]
list2 = [10, 11]
listadd = list1 + list2  # 리스트 + 리스트 = 하나의 리스트로 결합
print(listadd)
listmulti = list2 * 3  # 리스트 * 숫자 = 반복
print(listmulti)

# 리스트 순회 예제
lol = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8, 9]
]
print((lol[0]))
print((lol[2][1]))

for sub in lol:
    for item in sub:
        print(item, end=' ')
    print()

# 이중 리스트 예제
score = [
    [88, 76, 92, 98],
    [65, 70, 58, 82],
    [82, 80, 78, 88]
]


def getSubjectScore(student):
    subject_total = 0  # 여기를 함수로 구현하기
    for subject in student:
        subject_total += subject

    return subject_total


def getAvg(subject_total, student):
    subjects = len(student)  # 과목의 수

    print("총점 %d, 평균 %.2f" % (subject_total, subject_total / subjects))
    # avg = subject_total / subjects
    # print(f"총점 {subject_total}, 평균 {avg:.2f}")와 같음 권장!!

    return subjects


def main():

    total = 0
    totalsub = 0
    for student in score:
        subject_total = getSubjectScore(student)

        subjects = getAvg(subject_total, student)

        total += subject_total
        totalsub += subjects

    print("전체평균 %.2f" % (total/totalsub))  # '%.2f'는 소수점 두번째 자리까지
    # total_avg = total/totalsub
    # print(f"전체평균 {total_avg}")와 같음 권장!!

main()


# 문자열 + 숫자는 오류
# 연결하려면 숫자를 str 형으로 형변환 후 +
