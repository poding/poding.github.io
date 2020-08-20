# 실행 멈춤
import time

print("안녕하세요")
# time.sleep(1)
print("밤에 성시경이 두 명 있으면 무엇일까요?")
# time.sleep(5)
print('야간 투시경입니다.')

# 달력
import calendar as cal

print(cal.calendar(2020))
print(cal.month(2020, 7))

dates = ["월", "화", "수", "목", "금", "토", "일"]

day = cal.weekday(2020, 8, 15)
print("광복절은 %s요일입니다." %dates[day])

# 날짜를 문자열로 변환
# 보통 사진 파일명으로 많이 씀
import time
from datetime import datetime

print(time.strftime('%Y-%m-%d %I:%M'))

timestring = '2019-02-20 12:12:12'
print(time.strptime(timestring, '%Y-%m-%d %I:%M:%S'))

now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S.%f"))  # %f 사용하면 소수점 6자리까지 출력

for i in range(1, 11):
    print(now.strftime(f"%Y-%m-%d %H:%M:%S-{i:03d}.jpg"))
# f로 포맷팅문자열 이용
# f는 {}와 연결, 자리수는 3자리 빈자리있으면 0으로 채우겠다는 의미미
