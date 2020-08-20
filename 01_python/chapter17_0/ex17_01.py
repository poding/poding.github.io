# 열거 가능 객체 (literable)
# for 문의 시퀀스로 사용 가능
nums = [11, 22, 33]

it = iter(nums)
while True:
    try:
        num = next(it)  # 다음 요소 추출
    except StopIteration:  # 요소가 없는데 next 호출하는 경우
        break
    print(num)


class Seq:
    def __init__(self, data):
        self.data = data
        self.index = -2

    def __iter__(self):  # iter, next 가지면 나의 객체도 포문의 시퀀스로 쓸 수 있음
        return self

    def __next__(self):
        self.index += 2
        if self.index >= len(self.data):
            # self.index = -2  포문 두번 돌렸을 때 출력 가능
            raise StopIteration

        return self.data[self.index:self.index+2]


solarterm = Seq("입춘우수경칩춘분청명곡우입하소만망종하지소서대서")

for k in solarterm:
    print(k, end=',')

for k in solarterm:  # 포문 두번 돌리면 한번만 출력
    print(k, end=',')
