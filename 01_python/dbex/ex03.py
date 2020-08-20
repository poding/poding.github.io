import MySQLdb

db = MySQLdb.connect(host='localhost', db='employees', user='root', passwd='1234', charset='utf8')

cursor = db.cursor()
print("접속에 성공했습니다")

cursor.execute('DROP TABLE IF EXISTS tblAddr')

cursor.execute("""
CREATE TABLE tblAddr(
name CHAR(16) PRIMARY KEY,
phone CHAR(16),
addr TEXT)
""")

cursor.execute("INSERT INTO tblAddr VALUES('김상형', '123-4567','오산')")
cursor.execute("INSERT INTO tblAddr VALUES('한경은', '555-1004','수원')")
cursor.execute("INSERT INTO tblAddr VALUES('한주원', '444-1092','대전')")

cursor.execute("SELECT * FROM tblAddr order by addr")
table = cursor.fetchall()
print(type(table),table)

for record in table:
    print(record)
    print(f"이름: {record[0]}, 전화 : {record[1]}, 주소 : {record[2]}")


cursor.execute("SELECT addr FROM tblAddr WHERE name = '김상형'")
record = cursor.fetchone()

if record : print(f"김상형은 {record[0]}에 살고 있습니다.")
else : print("김상형은 없는 이름입니다")

db.commit()

cursor.close()
db.close()