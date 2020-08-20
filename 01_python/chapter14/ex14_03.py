# 한꺼번에 읽지 않고 끊어서 읽기
# f = open("live.txt", "rt")
# while True:
#    text = f.read(10)
#     if len(text) == 0: break  # 루프 끝나는 조건
#     print(text, end="")
# f.close()

# 1K = 1024

# 한 줄씩 읽기(개행문자 붙어있음)
f = open("live.txt", "rt", encoding="utf8")
text = ""
line = 1
while True:
    row = f.readline()
    if not row: break
    text += str(line) + " : " + row
    line += 1

f.close()
print(text)

# 리스트를 리턴하는 readlines
f = open("live.txt", "rt", encoding="utf8")
rows = f.readlines()

for row in rows:
    print(row, end="")
f.close()

# enumerate 사용
f = open("live.txt", "rt", encoding="utf8")
rows = f.readlines()

for ix, row in enumerate(rows):
    print(f"{ix} : {row}", end="")
f.close()
