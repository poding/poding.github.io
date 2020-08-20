def calcrage(begin, end):
    total = 0
    for num in range(begin, end+1):
        total +=num
    return total


print("3~7 = ", calcrage(3,7))

def printsum(n):
    total = 0
    for num in range(n+1):
        total += num
        print("~",n,"=",total)


printsum(4)
printsum(10)

def calcstep(begin, end, step=1):
    total = 0
    for num in range(begin, end+1,step):
        total += num
    return total
print("1 ~ 10 =",calcstep(1,10,2))
print("2~10 =",calcstep(1,100))
