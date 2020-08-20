# 데이터 입력 받은 후 추가
import MySQLdb

db = MySQLdb.connect(host='localhost', db='employees', user='root', passwd='9422', charset='utf8')
cursor = db.cursor()

try:
    print("데이터 추가============")

    name = input("이름: ")
    phone = input("전화번호: ")
    addr = input("주소: ")
    print("======================")

    sql = "insert into tblAddr values(%s, %s, %s)"

    cursor.execute(sql, (name, phone, addr))

    db.commit()
    print("추가 완료==============")
except Exception as e:
    print(e)

cursor.close()
db.close()

# 기본키 컬럼이 중복되거나, 길이를 초과하거나, 타입 안맞거나 하면 에러 -> 예외처리 해줘야 함
