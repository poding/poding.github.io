import MySQLdb

db = MySQLdb.connect(host='localhost', db='employees', user='root', passwd='1234', charset='utf8')

cursor = db.cursor()

print("데이터추가====================")
name = input("이름: ")
phone = input("전화번호: ")
addr = input("주소: ")
print("=============================")

sql = "INSERT INTO tblAddr VALUES(%s,%s,%s)"

cursor.execute(sql, (name, phone, addr))

db.commit()
print("추가 완료")



#필요한 작업 실행

cursor.close()
db.close()