# 컴프리핸션 예제
print([n for n in range(1, 11)])

nums = [n*2 for n in range(1, 11)]
for i in nums:
    print(i, end=',')


nums = []
for n in range(1, 11):
    nums.append(n*2)
print()
print(nums)

print([n for n in range(1, 11) if n % 3 == 0])

# 컴프리핸션의 대상이 되는 패턴
# nums = []
# for v in 시퀀스:
#   ...
#   value = ...
#   nums.append()


# 튜플은 () 생략가능, 추가수정삭제 불가능
score = 88, 95, 70, 100, 99
print(score)
score = 88,  # (88, )이랑 같음 튜플 OOO
print(score)
score = 88  # (88)이랑 같음 튜플 XXX
print(score)

lee, kim, kang = "이순신", "김유신", "강감찬"  # 튜플 사용
print(lee)
print(kim)
print(kang)
