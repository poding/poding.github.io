from addr_models import Addr

class AddressRepository:
    def __init__(self,db):
        self.cursor = db.cursor()

    def close(self):
        self.cursor.close()

    #데이터 건수를 구해주는 메소드
    def get_total(self,where=''):
        sql = "select count(*) from tblAddr " + where
        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        return row[0]

    def get_list(self, where=''):
        sql = "select * from tblAddr "+ where
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return (Addr(*row) for row in rows)

    def get_one(self, name):
        sql = "select * from tblAddr where name = %s"
        self.cursor.execute(sql, (name,))
        row = self.cursor.fetchone()
        addr = Addr(*row) #모델클래스 생성, 인스턴스화
                          # **는 사전 앞에, 키워드 전달 방식으로 호출
        return addr

    def insert(self, data):
        sql = "insert into tblAddr values(%s,%s,%s)"
        self.cursor.execute(sql, (data.name, data.phone, data.addr))

    def remove(self, name):
        sql = "delete from tblAddr where name = %s"
        return self.cursor.execute(sql, (name,))

    def update(self, data):
        sql = "update tblAddr set phone=%s, addr=%s where name = %s"
        self.cursor.execute(sql, (data.phone, data.addr, data.name))

