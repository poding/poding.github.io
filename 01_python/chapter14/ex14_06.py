# 보조자료 14.2
try:
    with open('test.txt', 'r') as file:  # close() 함수 사용 시 예외 발생될 수 있어서
        # close() 함수 없이도 파일 닫힘
        text = file.read()
        print(text)
except FileNotFoundError:
    print("파일이 없습니다.")
    
    
# ex14_04의 저장 함수를 close() 사용없이 with ~ as 문 사용
def save(fpath, data):
    try:
        with open(fpath, "wt") as f:  # f = open(fpath, "rt")와 동일
            for l in data:
                l = map(str, l)
                row = ','.join(l)
                f.write(row + "\n")
    except Exception as e:
        print(e)  

# pickle 모듈
# 파이썬 자료형 그대로 저장, 그대로 로드
import pickle


def save(fpath, data):
    try:
        with open(fpath, 'wb') as file:
            pickle.dump(data, file)
    except Exception as e:
        print(f"{fpath} 파일 쓰기에 실패했습니다.")
        print(e)


def load(fpath):
    try:
        with open(fpath, 'rb') as file:
            data = pickle.load(file)
            return data
    except:
        print(f"{fpath} 파일 읽기에 실패했습니다.")


def main():
    data = [
        [1, 2, 3, 54, 45],
        [7, 8, 3, 4, 5],
        [1, 12, 13, 4, 25]
    ]

    save("data2.dat", data)

    data2 = load("data2.dat")
    print(data2)

# 이렇게 하면 에러 남
# def main():
#     data = [
#         [1, 2, 3, 54, 45],
#         [7, 8, 3, 4, 5],
#         [1, 12, 13, 4, 25]
#     ]

#     save("./data/dat2.dat", data) 디렉터리 오류

#     data2 = load("./data/data2.dat")
#     print(data2)


main()

