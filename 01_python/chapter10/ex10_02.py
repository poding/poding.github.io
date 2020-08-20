# 집합
print(set('aabbbcccc'))
print(set([12, 34, 56, 78]))
print(set(('홍길동', '고길동', '둘리')))  # 순서는 랜덤
print(set({'boy': '소년', 'school': '학교'}))
print(set)

# 집합 연산
twox = {2, 4, 6, 8, 10, 12}
thrreex = {3, 6, 9, 12, 15}

print("교집합", twox & thrreex)
print("합집합", twox | thrreex)
print("차집합", twox - thrreex)
print("차집합", thrreex - twox)
print("배타적 차집합", twox ^ thrreex)




