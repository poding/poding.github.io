# data 리스트를 data.csv 라는 파일명으로 저장하기
def save(fpath, data):
    f = open(fpath, "wt")
    for l in data:
        l = map(str, l)  # int형을 문자형으로 변환 이런게 떠올라야 코딩이 쉬워짐
        row = ','.join(l)
        f.write(row + "\n")
    f.close()


def load(fpath):
    f = open(fpath, "rt")
    lines = f.readlines()  # 전체 줄 읽기
    data = []
    for line in lines:
        print(line, end='')  # 숫자가 아닌 한 개의 문자열, end 안쓰면 개행문자때문에 빈줄이 들어감
        row = line.split(',')  # 컴마를 기준으로 요소들을 리스트로 변환
        print(row)
        row = list(map(int, row))  # split 된 문자열 요소를 정수 요소로 반환
        print(row)
        data.append(row)
    f.close()
    return data


def main():
    data = [  # 이건 데이터 ,가 아님 파일에서는 데이터로 ,가 존재
        [1, 2, 3, 54, 45],
        [7, 8, 3, 4, 5],
        [1, 12, 13, 4, 25]
    ]\

    save("data.csv", data)

    data = load("data.csv")
    print(data)


main()
