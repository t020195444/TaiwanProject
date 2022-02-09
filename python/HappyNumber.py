import sys
q = sys.stdin.read()
data = q.splitlines()


def getsum(num):
    numst = str(num)
    sum = 0
    for i in numst:
        sum += int(i)**2
    return sum


for i in range(1, len(data)):
    n = data[i]
    while getsum(n) != 1 and getsum(n) != 4:
        n = getsum(n)
    else:
        if(getsum(n) == 1):
            print("T")
        else:
            print("F")
