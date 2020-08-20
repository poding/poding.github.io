# update, delete
import MySQLdb

db = MySQLdb.connect(host='localhost', db='employees', user='root', passwd='9422', charset='utf8')
cursor = db.cursor()

print("접속에 성공했습니다.")

cursor.execute("update tblAddr SET addr = '제주도' where name = '김상형'")
cursor.execute("delete from tblAddr where name = '권혜주'")

db.commit()

cursor.close()
db.close()
