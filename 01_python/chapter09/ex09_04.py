# 큐, 스택 삭제 예제
score = [88, 95, 70, 100, 99]
score.append(50)
print('큐', score)  # 큐는 맨 앞의 데이터 삭제, FIFO
print('큐', score.pop(0))
print('큐', score)

score = [88, 95, 70, 100, 99]
score.append(50)
print('스택', score)  # 스택은 맨 뒤의 데이터 삭제, LIFO
print('스택', score.pop())
print('스택', score)

# 리스트 검색 예제
ans = input("결제 하시겠습니까? ")
if ans in ['yes', 'y', 'ok', '예']:  # 값이 시퀀스에 포함되어 있는지 True/False 로 리턴
    print("결제를 진행합니다.")
else:
    print("결제를 취소합니다.")

# 리스트 정렬 예제
score = [88, 95, 70, 100, 99]
score.sort()  # 디폴트 값은 오름차순
print(score)
score.reverse()
print(score)

country = ["Korea", "japan", "CHINA", "america"]
country.sort()
print(country)
country.sort(key=str.lower)  # lower 로 각각 소문자로 변환시킨 후에 정렬(원본 변화 X)
print(country)
# 원본 변화없이 소문자로 출력은 이렇게
for c in country:
    print(c.lower(), end=', ')


score = [88, 95, 70, 100, 99]
sorted_score = sorted(score)  # 원본 유지되기 때문에 별도의 변수에 대입
print(score)
print(sorted_score)

score = [88, 95, 70, 100, 99]
sorted_score = sorted(score, reverse=True)  # 내림차순 정렬
print(score)
print(sorted_score)