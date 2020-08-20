# 읽기 특징
try:
    # 문자 코드를 디코딩할 수 없음의 오류가 뜸->인코딩 옵션 추가
    # f = open("live.txt", "rt", encoding="utf8") # 상대경로
    # f = open("\\temp\\live.txt", "rt", encoding="utf8")  # 절대경로
    f = open("test1./t.txt", "rt", encoding="utf8")  # edit에서 워킹스페이스를 temp로 옮긴 후
    text = f.read()
    print(text)
except FileNotFoundError:
    print("파일이 없습니다.")
finally:
    f.close()  # f라는 변수 자체가 생성 안됨

# 상대 경로는 워킹 디렉토리를 기준으로 함, 워킹 디렉토리 위치에 따라 다름
# 절대 경로는 루트부터 경로 기술
