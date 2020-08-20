import MySQLdb

db = MySQLdb.connect(db='employees', host='localhost', user='root', passwd='1234', charset='utf8')
rla
cursor = db.cursor()

print("접속에 성공했습니다")
name = input("검색어(이름): ")

cursor.execute(f"SELECT addr FROM tblAddr WHERE name = '{name}'")
record = cursor.fetchone()

if record : print(f"{name}은 {record[0]}에 살고있습니다.")
else : print(f"{name}은 없는 이름입니다.")

cursor.close()
db.close()