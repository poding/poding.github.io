import MySQLdb

db = MySQLdb.connect(host='localhost', db='employees', user='root', passwd='1234', charset='utf8')

cursor = db.cursor()

name = input("검색어(이름) : ")


sql = "SELECT addr FROM tblAddr WHERE name = %s"
cursor.execute(sql,(name,))

record = cursor.fetchone()
cursor.execute(sql)

#필요한 작업 실행

cursor.close()
db.close()