import sys

import MySQLdb

from myapp import Application, MenuItem
from addr_repository import AddressRepository
from addr_ui import *
#*은 모든 함수를 다 임포트하겠다는 뜻임
from addr_ui import *
#파이썬 표준 모듈이라 따로 설치할 필요가없다 mysql과는 다르게.
import sqlite3

class DBApp(Application,MenuItem):
    def __init__(self):
        super().__init__()
        #self.db = MySQLdb.connect(db='employees', host='localhost', user='root', passwd='1234',charset='utf8')
        self.db = sqlite3.connect("c:/temp/test.db")
        self.repo = AddressRepository(self.db)

        

    def create_menu(self, menu):
        menu.add(MenuItem("목록", self.print_list))
        menu.add(MenuItem("검색",self.search))
        menu.add(MenuItem("추가", self.add))
        menu.add(MenuItem("수정", self.update))
        menu.add(MenuItem("삭제", self.remove))
        menu.add(MenuItem("종료", self.exit))

    def print_list(self):


            #어플리케이션(현재 파일)은 세부기능을 하위모듈에 전가시키고
            #자기 자신은 기능을 실행하기위해 어떤순서로 기능을 써먹느냐
            #호출,흐름제어만 담당한다
            total = self.repo.get_total()
            rows = self.repo.get_list()
            print_list(total,rows)

    def search(self):
            name = input("이름: ")
            where = f"where name like '%{name}%'"
            total = self.repo.get_total(where)
            rows = self.repo.get_list(where)
            if not rows:
                print(f"{name} 데이터가 없습니다")
                return
            print_list(total,rows)

    def add(self):
            data = input_addr_info()
            self.repo.insert(data)
            self.db.commit()
            print("추가 완료")

    def update(self):
            name = input("이름 : ")
            data = self.repo.get_one(name)

            if not data:
                print(f"{name} 데이터가 없습니다")
                return

            data = input_new_addr(data)
            self.repo.update(data)
            self.db.commit()
            print("수정 완료")


    def remove(self):
            name = input("이름: ")
            self.repo.remove(name)
            self.db.commit()
            print("삭제완료")

    def exit(self):
        answer = input("종료하시겠습니까?([y] / [n])")
        if answer in ["y","Y",""]:
            self.repo.close()
            self.db.close()
            sys.exit(0)

if __name__ == '__main__':
    app = DBApp()
    app.run()

