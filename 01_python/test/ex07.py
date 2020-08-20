import sys
import MySQLdb
from myApp import Application, MenuItem

class DBApp(Application):
    def __init__(self):
        super().__init__()  # 부모클래스 생성자 호출
        self.db = MySQLdb.connect(host='localhost', db='employees', user='root', passwd='9422', charset='utf8')
        self.cursor = self.db.cursor()  # 인스턴스 변수로 관리

    def create_menu(self, menu):
        menu.add(MenuItem("목록", self.print_list))
        menu.add(MenuItem("추가", self.add))
        menu.add(MenuItem("수정", self.update))
        menu.add(MenuItem("삭제", self.remove))
        menu.add(MenuItem("종료", self.exit))

    def exit(self):
        answer = input("종료하시겠습니까?(y/n) ")
        if answer in ["y", "Y"]:
            self.cursor.close()
            self.db.close()
            sys.exit(0)

    def print_list(self):
        print("목록보기")


    def add(self):
        print("추가하기")

    def update(self):
        print("수정하기")

    def remove(self):
        print("삭제하기")


if __name__ == '__main__':
    app = DBApp()
    app.run()
