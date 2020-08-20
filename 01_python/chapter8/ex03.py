# nums = [0,1,2,3,4,5,6,7,8,9]
# nums[6:6] = [60,70,80,90]#기존값을 삭제하지않고 출력됨
# print(nums)
#
# nums[2:5] = [20,30,40]
# print(nums)
# nums[6:8] = [60,70,80,90]
# print(nums)

#문자열은 불변이라서 이렇게 대입연산이 안됨(읽기는 되지만 쓰기는 안됨)



lol = [[1,2,3],[4,5],[6,7,8,9]]
print(lol[0])
print(lol[2][1])

for sub in lol:
    for item in sub:
        print(item, end='')
    print()




score = [
    [88,76,92,98],
    [65,70,58,82],
    [82,80,78,88]
]
total = 0
totalsub =0

def getSubject_total(*student):
    subject_total = 0
    for subject in student:
        subject_total += subject
    return subject_total



def printAvg(student,subject_total):
    subjects = len(student)#과목의수
    avg = subject_total/subjects
    #print("총점 %d,평균 %.2f" % (subject_total,subject_total/subjects))
    print(f"총점 {subject_total},평균{avg:.2f}")
    return subjects

def main():
    total = 0
    totalsub = 0
    for student in score:
        subject_total = getSubject_total(student)

        subjects = printAvg(student,subject_total)
        total += subject_total
        totalsub += subjects

    total_avg = total / totalsub
    print(f"전체평균{total_avg}")

main()

