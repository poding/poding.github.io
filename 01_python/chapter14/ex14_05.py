# 입출력 위치
# f = open("live.txt", "at")

# f.seek(12, 0)  # 글자 중간에 걸치면 예외발생
# text = f.read()
# f.close()

# print(text)

f = open("live.txt", "at", encoding="utf8")  # w 대신 a 사용하면 파일에 내용 추가
f.write("\n푸쉬킨 형님의 말씀")
f.close()