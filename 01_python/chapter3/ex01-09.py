print(None, bool(None))
print(0,bool(0))
print("",bool(""))
print([],bool([]))
print((),bool(()))

a=3
b=4
if a ==3 and b==4:
    print("OK")

a=3
b=5
if a==3 or b==4:
    print("OK")
a=3
if a>1 and a<10:
    print("OK")
if 1<a<10:
    print("OK")

age = 16
if age<19:
    print("애들아 가라")

age=24

if age<19:
    print("애들은 가라")
elif age<25:
    print("대학생입니다")
else:
    print("들어오세요")


man = True
age = 22

if man == True:
    if age>19:
        print("성인 남자입니다.")
    else:
        print("미성년 남자입니다")
else:
    if age>19:
        print("성인 여자입니다.")
    else:
        print("미성년 여자입니다")