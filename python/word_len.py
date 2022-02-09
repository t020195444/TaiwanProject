import sys
q = sys.stdin.read()
data = q.splitlines()
total = 0
save = 0
for j in range(0, len(data)):
    for i in data[j]:
        if save <= int(i):
            save = int(i)
            total += 1
        else:
            save = 0
            total = 1
    print(total)
