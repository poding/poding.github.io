# 표준모듈
import math
print(math.sqrt(2))

from math import sqrt
print(sqrt(2))

import math as m
print(m.sqrt(2))

from math import sqrt as sq
print(sq(2))

# 시간 모듈
import time
print(time.time())  # 1970/1/1/자정으로부터 경과 시간 초로 표현

t = time.time()
print(time.ctime(t))
print(time.localtime(t))

now = time.localtime()
print("%d년 %d월 %d일" % (now.tm_year, now.tm_mon, now.tm_mday))
print("%d:%d:%d" % (now.tm_hour, now.tm_min, now.tm_sec))

import datetime
now = datetime.datetime.now()
# 이걸 더 많이 씀
# from datetime import datetime
# now = datetime.now()
print("%d년 %d월 %d일" % (now.year, now.month, now.day))
print("%d:%d:%d" % (now.hour, now.minute, now.second))

# 실행시간 측정
import time

start = time.time()
for a in range(1000):
    print(a)
end = time.time()

print(end - start)

total = 0
for a in range(1000):
    total += a
end = time.time()

print(end - start)