# 데이터 추가, 출력
import MySQLdb

db = MySQLdb.connect(host='localhost', db='employees', user='root', passwd='9422', charset='utf8')
cursor = db.cursor()

print("접속에 성공했습니다.")

sql = """
CREATE TABLE tblAddr(
    name CHAR(16) PRIMARY KEY,
    phone CHAR(16),
    addr TEXT
)
"""
cursor.execute('DROP TABLE IF EXISTS tblAddr')
cursor.execute(sql)

cursor.execute("INSERT INTO tblAddr VALUES('김상형', '123-4567', '오산')")
cursor.execute("INSERT INTO tblAddr VALUES('한경은', '123-4567', '수원')")
cursor.execute("INSERT INTO tblAddr VALUES('한주완', '123-4567', '대전')")

db.commit()

cursor.execute("SELECT * FROM tblAddr ORDER BY addr")

# where 절이 없는 select 문은 보통 fetchall 로 처리
# where 절 있으면 fetchone / fetchall

table = cursor.fetchall()  # 전체 꺼내올 때, 하나씩 꺼내올 때는 fetchone(무한루프 돌릴 때)
for record in table:  # table 타입도 튜플
    print(record)  # record 타입은 튜플
    print(f"이름: {record[0]}, 전화: {record[1]}, 주소: {record[2]}")

cursor.close()
db.close()
