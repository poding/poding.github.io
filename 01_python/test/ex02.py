import MySQLdb

db = MySQLdb.connect(host='localhost', db='employees', user='root', passwd='9422', charset='utf8')
cursor = db.cursor()

print("접속에 성공했습니다.")

sql = """
select addr from tblAddr where name = '김상형'
"""
cursor.execute(sql)

record = cursor.fetchone()
# fetchall 에서 데이터가 없으면 비어있는 튜플 리턴(데이터 있건 없건 튜플)
# 따라서 반드시 검사 후에 출력
if record : print(f"김상형은 {record[0]}에 살고 있습니다.")
else : print("김상형은 없는 이름입니다.")

cursor.close()
db.close()
