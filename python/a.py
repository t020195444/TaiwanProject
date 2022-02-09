import sys
import math
q = sys.stdin.read()
q1 = q.split(" ")

ma2 = []
ma3 = []
ma5 = []
int_q1 = list(map(int, q1))

for i in range(len(int_q1)-1):
    sum = 0
    sum = (int_q1[i] + int_q1[i+1])/2
    ma2.append(math.ceil(sum))

for i in range(len(ma2)-1):
    sum = 0
    sum = (ma2[i] + ma2[i+1])/2
    ma3.append(math.floor(sum))
for i in range(len(ma3)-1):
    sum = 0
    sum = (ma3[i] + ma3[i+1])/2
    ma5.append(math.floor(sum))

a = " ".join([str(_) for _ in ma2])
b = " ".join([str(_) for _ in ma3])
c = " ".join([str(_) for _ in ma5])
print(a)
print(b)
print(c)
