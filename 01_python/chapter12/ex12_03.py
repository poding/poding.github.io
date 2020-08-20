# 랜덤 모듈
import random

for i in range(5):
    print(random.randint(1, 10))  # 1~10까지 정수

for i in range(5):
    print(random.randrange(1, 10))  # 1~9까지 정수

for i in range(5):
    print(random.uniform(1, 10))  # 1~10까지 실수

# 시퀀스에서 랜덤한 요소 선택 두가지 예제
food = ["짜장면", "짬뽕", "탕수육", "군만두"]
print(random.choice(food))

i = random.randrange(len(food))
print(food[i])

# 시퀀스 내용 랜덤하게 섞기
print(food)
random.shuffle(food)
print(food)

# 시퀀스에서 랜덤한 갯수의 요소  뽑기
print(random.sample(food, 2))

nums = random.sample(range(1, 46), 6)  # 로또
nums.sort()
print(nums)

# sys 모듈 (읽기 전용)
import sys

print("버전: ", sys.version)
print("플랫폼: ", sys.platform)
print("바이트 순서: ", sys.byteorder)
print("모듈 경로: ")
for i in range(len(sys.path)):
    print(sys.path[i], end="\n")
# for path in sys.path:
#     print(path)

# sys.exit(0)  # 위에껀 변수 이건 함수, 프로그램 강제 종료
# sys.exit(-1)  # 종료 코드 -1

# 명령형 인수
print(sys.argv)  # [파일경로, 인자1, 인자2, ..)
