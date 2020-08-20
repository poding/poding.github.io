import MySQLdb

db = MySQLdb.connect(host='localhost', db='employees', user='root', passwd='1234', charset='utf8')

cursor = db.cursor()


cursor.execute("UPDATE tblAddr SET addr = '제주도' WHERE name ='김상형'")
db.commit()

cursor.close()
db.close()