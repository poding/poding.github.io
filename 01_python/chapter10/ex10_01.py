# 키 중복 불가, 중복되면 업데이트로 간주
# 사전 활용 예제
song = """by the rivers of babylon, there we sat down
yeah we wept, when we remember zion.
when the wicked carried us away in captivity
required from us a song
now how shall we sing the lord's song in a strange land"""

alphabet = dict()
for c in song:
    if c.isalpha() == False:
        continue

    c = c.lower()
    if c not in alphabet:
        alphabet[c] = 1
    else:
        alphabet[c] += 1


def getValue(x):  # x는 튜플로 가정
    return x[1]  # 튜플의 두번째 값 리턴


alphabetList = list(alphabet.items())

# alphabetList.sort(key=getValue, reverse=True)  # 괄호 없으니까 함수 전달, 호출 XX
# 람다로 표현하면?
alphabetList.sort(key=lambda x: x[1], reverse=True)

# for item in alphabetList:  # reverse 빼면 오름차순
#     print(item)
# 위에 꺼 포맷팅한 표현
for a, c in alphabetList:
    print(f"{a} : {c}")

# 예제1
print(alphabet)

key = list(alphabet.keys())
key.sort()
for c in key:
    num = alphabet[c]
    print(c, '=>', num)

