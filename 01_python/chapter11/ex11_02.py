# 람다 함수 예제
# 인수:식
lambda x: x + 1

def increase(x):
    return x + 1


score = [45, 89, 72, 53, 94]
for s in filter(lambda x: x < 60, score):  # 파이썬 람다는 한줄로만 표현할 수 있음
    print(s)  # 리턴 생략


score = [45, 89, 72, 53, 94]
for s in map(lambda x: x / 2, score):
    print(s, end=", ")

# 리스트의 사본 예제
# 리스트는 복사본이 없음 변경하면 같이 바뀜, 실제 데이터는 힙에 있고 참조하는 것
# 복사해서 다른 쪽에 영향을 미치지 않게 하려면?
list1 = [1, 2, 3]
list2 = list1.copy()  # list2 = list1[:]과 같음 (전체 슬라이싱)

print(list1 == list2)

list2[1] = 100
print(list1)
print(list2)

print(list1 == list2)

# 얕은 복사 (거의 대부분 사용, 속도 빠름)
list0 = ['a', 'b']
list1 = [list0, 1, 2]  # list0은 데이터가 들어가는게 아니라 주소값 참조
list2 = list1.copy()

list2[0][1] = 'c'
list2[1] = -1

print(list1)
print(list2)
print(list0)

# 깊은 복사 (데이터 조작에 안전)
import copy

list0 = ['a', 'b']
list1 = [list0, 1, 2]
list2 = copy.deepcopy(list1)  # 새로운 카피본 생성

list2[0][1] = 'c'
print(list1)
print(list2)
