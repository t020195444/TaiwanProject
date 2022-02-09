import sys
q = sys.stdin.read()
q1 = q.splitlines()
li = []
gcd = 1
num = 10000
for i in range(1, len(q1)):
    li = []
    num = 10000
    data = q1[i].split(",")
    for j in data:
        li.append(int(j))
        if(int(j) < num):
            num = int(j)
    for i in range(1, num+1):
        if((int(j) % i == 0) and (num % i == 0)):
            gcd = i
    print(gcd)
