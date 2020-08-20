# 데이터 검색
import MySQLdb
db = MySQLdb.connect(host='localhost', db='employees', user='root', passwd='9422', charset='utf8')
cursor = db.cursor()

print("접속에 성공했습니다.")

name = input("검색어(이름): ")

# cursor.execute(f"select addr from tblAddr where name = '{name}'")  # ''꼭 감싸줘야 함(파이썬 기준 아니고 sql 기준)
# 아니면 밑에처럼 표기할 수도 있음 (여러개일 때는 이게 더 편함)
sql = "select addr from tblAddr where name = %s"
cursor.execute(sql, (name,))  # execute 의 두번째 인자로 전달, 튜플이기 때문에 (), 인자 하나이면 ',' 추가
record = cursor.fetchone()

if record : print(f"{name}은 {record[0]}에 살고 있습니다.")
else : print(f"{name}은 없는 이름입니다.")


cursor.close()
db.close()
