# 모듈 예제
# 재사용될 때 모듈 사용
INCH = 2.546


def calcsum(n):
    sum = 0
    for num in range(n+1):
        sum += num

    return sum

# if __name__ == "__main__" :
#     print("1inch = ", INCH)
#     print("~10 = ", calcsum(10))


print("util", __name__)  # name 은 파일명 출력
if __name__ == '__main__':  # True : 이 파일에서는 모듈이 아님, False : 모듈 실행
    print("Hello util")