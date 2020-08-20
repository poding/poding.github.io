# 리스트 추가 예제
nums = [1, 2, 3, 4]
nums.append(5)  # 리스트 끝에 값 추가, 이게 더 사용빈도 높음
print(nums)

nums.insert(2, 99)  # 2번째 위치에 값 추가
print(nums)

# 랜덤한 리스트 예제
import random

def rand(start, end):
    return int(random.random()*(end-start + 1)) + start


def getRandomList(start, end, count):
    nums = []
    for _ in range(count):  # 루프 돌릴 때 변수가 사용되지 않는 경우에 _ 사용
        r = rand(start, end)  # r = random.randint(1, 100)
        nums.append(r)

    return nums


def main():
    lst = getRandomList(1, 100, 10)
    # 컴프리핸션으로 표현하면?
    # lst = [rand(1, 100) for _ in range(6)]
    # 리스트 리터럴 안에서 루프
    print(lst)


main()


# 리스트 삽입 예제
nums = [1, 2, 3, 4]
nums[2:2] = [90, 91, 92]
print(nums)

nums = [1, 2, 3, 4]
nums[2] = [90, 91, 92]
print(nums)

list1 = [1, 2, 3, 4, 5]
list2 = [10, 11]
list3 = list1 + list2
print(list3)
list1.extend(list2)  # 기존에 있는 거에 추가
print(list1)

# 리스트 삭제 예제01
score = [88, 95, 70, 100, 99, 88, 78, 50]
score.remove(100)  # 값 삭제, delete 는 해당 위치 삭제
print(score)

del(score[2])
print(score)

score[1:4] = []
print(score)

# 리스트 삭제 예제02
score = [88, 95, 70, 100, 99]
print(score.pop())  # 끝 요소 삭제하고 삭제 값 리턴
print(score.pop())
print(score.pop(1))
print(score)
