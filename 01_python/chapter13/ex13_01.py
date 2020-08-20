# 예외 처리
# 예외 : 복구 가능
# 에러 : 복구 불가능
def test(str):
    try:
        score = int(str)
        print(score)
    except ValueError as e:  # as e 추가하면 더 자세한 에러 정보 출력, 밑에꺼보다 이게 더 나음
        e.print()
        print(e)

    except IndexError:
        print("첨자 범위를 벗어났습니다.")

    # except (ValueError, IndexError)
    print("작업완료")


def work():
    str = "89점"  # 에러발생
    # test(str)
    try:  # test에서 처리 안하고 여기서
        test(str)
    except Exception as e:
        print(e)


def work2():  # 에러발생 X
    str = "89"
    test(str)


def main():
    work()
    work2()


main()

# 임의로 예외 발생
def calcsum(n):
    if n < 0:
        raise ValueError  # 밑에 except 에러 객체랑 같아야 함

    total = 0
    for i in range(n+1):
        total += i
    return total

try:
    print("~10 =", calcsum(10))
    print("~-5 =", calcsum(-5))
except ValueError:
    print('입력값이 잘못되었습니다.')

