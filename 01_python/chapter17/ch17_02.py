def seqgen(data):  # __next()__ 에 해당되는 내용
    for index in range(0, len(data), 2):
        yield data[index:index+2]  # yield 는 루프 돌면서 계속 리턴


solarterm = seqgen("입춘우수경칩춘분청명곡우입하소만망종하지소서대서")  # 형태적으로는 함수와 같음
print(solarterm)  # 출력해보면 함수 실행되는게 아니라 객체로 변환시키겠다는 의미

for k in solarterm:
    print(k,end=',')