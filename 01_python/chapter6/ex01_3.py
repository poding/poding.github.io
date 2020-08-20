score = [92, 86, 68, -1, 56]
for s in score:
    if s == -1:

        continue
    print(s)

print('성적처리끝')

for dan in range(2,10):
    print(dan, "단")
    for hang in range(2,10):
        print(dan,'*',hang,'=',dan * hang)
    print()


for y in range(1,10):
    for x in range(y):
        print('*',end='')
    print()

for y in range(1,10):
    print('*'*y)

cnt=0
print("3 + 4 = ?")
while True:
    a = int(input('정답을 입력하세요'))
    if a==7 :
        print('참 잘했어요')
        break
    if cnt==2:
        print('맞추지 못했어요')
        break
    cnt +=1


def calsum(n):
    total = 0
    for num in range(n+1):
        total += num
    return total

print(" ~ 4 =",calsum(4))
print(" ~ 10 = ",calsum(10))



