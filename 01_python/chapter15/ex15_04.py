import pickle


class UserInfo:  # 순수한 데이터 저장용 클래스인 경우도 있음
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):  # 자세한 정보
        return f"< USER INFO {self.name} / {self.email} / {self.phone} >"

    def __repr__(self):  # 축약된 정보, 콜렉션에 프린트 할때 출력
        return f"< USER INFO {self.name} >"


class AddressBook():  # CRUD 순서로 떠올리면 됨
    def __init__(self):
        self.book = []  # 리스트 초기화

    def add(self, name, email, phone):
        ui = UserInfo(name, email, phone)  # 인스턴스 새로 생성
        self.book.append(ui)  # book.append(ui) 하면 지역변수 book 찾아서 에러

    def find_by_name(self, name):
        for ui in self.book:
            if ui.name == name:  # 이름이 존재하지 않으면 NONE 이 리턴
                return ui

    def search_by_name(self, name):  # 이름 일부가 동일한 거 찾아서 새로운 리스트 만들기
        new_book = []
        for ui in self.book:
            if ui.name.find(name) > -1:
                new_book.append(ui)
        return new_book

#   위에 꺼 컴프리핸션으로 바꾸면?
#   def search_by_name(self, name):
#       return [ui for ui in self.book if ui.name.find(name) > -1]

    def update(self, name, email, phone):
        ui = self.find_by_name(name)
        if not ui:
            print(f"{name}는(은) 목록에 없습니다.")
            return

        ui.email = email
        ui.phone = phone

    def remove(self, name):
        ui = self.find_by_name(name)
        if not ui:
            print(f"{name}는(은) 목록에 없습니다.")
            return

        self.book.remove(ui)

# pickle 활용한 파일 저장, 로드
    def save(self, fpath):
        try:
            with open(fpath, 'wb') as file:
                pickle.dump(self.book, file)
        except Exception as e:
            print(e)

    def load(self, fpath):
        try:
            with open(fpath, 'rb') as file:
                self.book = pickle.load(file)
        except Exception as e:
            print(e)

    def sort(self, reverse=False):  # 가나다 순으로 정렬, 오름차순
        self.book.sort(key=lambda u: u.name, reverse=reverse)  # 매개변수: 리턴값


# li = [
#     UserInfo("홍길동", "hong@naver.com", "010-1111-2222"),
#     UserInfo("고길동", "go@naver.com", "010-1111-3333")
# ]
#
# print(li)
#
# u1 = UserInfo("홍길동", "hong@naver.com", "010-1111-2222")
# u2 = UserInfo("고길동", "go@naver.com", "010-1111-3333")
#
# l = [u1, u2]
# print(l)  # 리스트에 있는 엘리먼트들을 출력 - repr
# print(l[0])

# file_name = 'book1.dat'
# addr_book = AddressBook()
# addr_book.add("졸려", "gae jolrue.com", "101-0000-1111")
# addr_book.add("너무졸려", "nermu jolrue.com", "101-0000-1111")
# addr_book.save(file_name)

# for ix in range(1, 100):
#     if ix % 2 == 0:
#         addr_book.add(f"홍길동{ix}", "hong{ix}@naver", '010-2222-1111')
#     else:
#         addr_book.add(f"고길동{ix}", "go{ix}@naver", '010-1111-2222')
# addr_book.save(file_name)

file_name = 'book1.dat'
addr_book = AddressBook()
addr_book.load(file_name)

addr_book.sort()
print(addr_book.book)

# addr_book2 = AddressBook()
# addr_book2.load(file_name)
# print(addr_book2.book)



# print(addr_book.book)
#
# u1 = addr_book.find_by_name('졸려')
# print(u1)
# u2 = addr_book.find_by_name('희동이')
# print(u2)
#
# addr_book.update('졸려', 'lalala.com', '010-2222-0000')
# u1 = addr_book.find_by_name('졸려')
# print(u1)
# addr_book.update('희동이', 'hahaha.com', '010-2222-3333')
#
# addr_book.remove('졸려')
# u1 = addr_book.find_by_name('졸려')
# print(u1)
#
# users = addr_book.search_by_name('길동')
# print(users)
# users = addr_book.search_by_name('졸')
# print(users)
