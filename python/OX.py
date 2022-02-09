import sys
q = sys.stdin.read()
data = q.splitlines()
for i in range(1, int(data[0])+1):
    anser = list(data[i])
    total = 0
    counter = []
    counter.append([anser[0], 1])
    for i in range(1, len(anser)):
        if(anser[i] != anser[i-1]):
            counter.append([anser[i], 1])
            total += 1
        else:
            counter[total][1] = counter[total][1]+1
        num = 0
        sum = 0
        to = 0
    for i in range(0, len(counter)):
        if counter[i][0] == 'O':
            sum = 0
            num = counter[i][1]
            for j in range(1, num+1):
                sum = sum + j
            to = sum + to
    print(to)
