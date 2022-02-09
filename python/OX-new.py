import sys
q = sys.stdin.read()
data = q.splitlines()
sum = 0
total = 0
for d in range(1, len(data)):
    datas = list(data[d])
    total = 0
    sum = 0
    for i in range(0, len(datas)):
        if (datas[i] == 'O'):
            sum = sum+1
            total = sum + total
        else:
            sum = 0
    print(total)
