def calcsum(n):
    total = 0
    for i in range(n+1):
        total+=i

    return total
help(calcsum(1))

def findMin(*numbers):
    min=999999
    for num in numbers:
        if min>=num:
            min = num
    return min
def findMax(*numbers):
    max=-999999
    for num in numbers:
        if max<=num:
            max=num
    return max

min = findMin(2,7,5,-1,20)
max = findMax(2,7,5,-1,20)
print('최소값:',min)
print('최대값:',max)
