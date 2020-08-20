# 자원의 정리 finally
def comm():
    try:  # 이렇게 하면 제대로 자원 정리가 안됨 그래서 finally
        print("네트워크 접속")
        d = 0
        if d != 0:
            return

        a = 2 / d
        print("네트워크 통신 수행")
    except:
        pass
    finally:  # try 벗어나면 반드시 실행 후 리턴
        print("접속 해제")

#   print("접속 해제")  # 예외 발생하던 안하던 접속 해제 근데 왜 굳이 finally 써야하는지?
    print("작업 완료")


def main():
    comm()

main()

# 자원의 정리 assert (단정문)
# 보통 테스트할 때 씀, 내가 원하는 값을 리턴할 수 있는지 보고 아니면 종료
score = 128
assert score <= 100, "점수는 100 이하여야 합니다."
print(score)

