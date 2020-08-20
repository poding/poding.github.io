# 배열 : 동일한 데이터 타입을 연속적인 공간에 저장해서 관리하는 자료형, numpy 사용
import numpy as np

data1 = [0, 1, 2, 3, 4, 5]
a1 = np.array(data1)  # 시퀀스 데이터(리스트, 튜플 등)을 배열로 변경
print(a1)

data2 = [0.1, 5, 4, 12, 0.5]
a2 = np.array(data2)
print(a2)

print(a1.dtype)  # 비트 수(디폴트는 정수 32비트)
print(a2.dtype)  # 실수는 64비트

#이 방법을 더 많이 씀
print(np.array([0.5, 2, 0.01, 8]))
print(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # 차원적으로 출력, 원래는 한줄로 쭉

