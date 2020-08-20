# note 구현
import sys


class MenuItem:
    def __init__(self, title, action=None):  # action 은 메뉴가 선택됐을 때 실행될 함수
        self.title = title
        self.action = action

    def __str__(self):  # print 에서 출력되는 내용
        return "< MenuItem {self.title} >"

    def __repr__(self):  # 컬렉션에 담겨있을 때 출력하는 축약 표현
        return "< MenuItem {self.title} >"

    def run(self):  # 메뉴 선택될 때 수행하는 함수
        self.action()


class Menu:  # MenuItem 에 대한 CRUD
    def __init__(self):
        self.menus = []

    def add(self, menu_item):  # 메뉴 추가
        self.menus.append(menu_item)

    def print(self):  # 메뉴 출력
        print("[메뉴] ", end="")
        for i, menu in enumerate(self.menus):
            print(f"{i}:{menu.title} ", end="")
        print()

    def run(self, select):  # 메뉴 선택
        if select >= len(self.menus):
            print("잘못된 메뉴 선택입니다.")
            return
        menu_item = self.menus[select]
        menu_item.run()  # self 는 select 번째에 있는 menu_item
        # self.menus[select].run()


# # 테스트
# menu = Menu()
# # 람다를 안쓰면?
# # action 에 해당하는 메뉴명 각각 함수에 print("열기 실행") 정의 해줘야 함
# # 번거로우니까 이름없는 함수 람다 사용
# item = MenuItem("열기"), lambda: print("열기 실행")  # 열기가 action
# menu.add(item)
# # 위에 두줄 간단히 사용하면?
# save = lambda: print("저장 실행")
# menu.add(MenuItem("저장"), save)
# menu.add(MenuItem("목록보기", lambda: print("목록보기 실행")))
# menu.add(MenuItem("종료", lambda: print("종료 실행")))
# menu.print()
#
# menu.run(1)  # 저장 메뉴 실행
# menu.run(3)  # 종료 메뉴 실행
# menu.run(4)  # 잘못된 메뉴

class Application:  # 부모 클래스
    def __init__(self):
        self.menu = Menu()
        self.create_menu(self.menu)

    def create_menu(self, menu):  # 틀만 잡아두고 자식 클래스에서 구현
        pass

    def run(self):
        while True:
            self.menu.print()
            sel = int(input("선택] "))
            self.menu.run(sel)


# 실제 기능을 제공하는 어플리케이션 클래스
class NotepadApp(Application):  # 상속된 자식 클래스, 추가 메서드만 구현, 변경이 필요하면 오버라이드
    def __init__(self):
        super().__init__()  # 부모 클래스의 생성자 호출출
        # self.menu = Menu()  # 메뉴 객체 생성
        # self.menu.add(MenuItem("열기", self.open))  # 그냥 open 하면 함수 호출, self.open 하면 메서드 호출
        # self.menu.add(MenuItem("저장", self.save))
        # self.menu.add(MenuItem("목록보기", self.print_list))
        # self.menu.add(MenuItem("종료", self.exit))

    def create_menu(self, menu):
        menu.add(MenuItem("열기", self.open))
        menu.add(MenuItem("저장", self.save))
        menu.add(MenuItem("목록보기", self.print_list))
        menu.add(MenuItem("종료", self.exit))

    def open(self):
        print("열기를 실행합니다.")

    def save(self):
        print("저장을 실행합니다.")

    def print_list(self):
        print("목록 보기를 실행합니다.")

    def exit(self):
        sys.exit(0)  # 정상적인 종료


class AddressBookApp(Application):  # 기능에 맞게 추가, 상속 이용해서 메서드 구현
    pass


def main():
    app = NotepadApp()  # 자식 클래스로 객체 생성
    app.run()

# if __name__ == "__main__": 모듈로 사용할 때

main()
