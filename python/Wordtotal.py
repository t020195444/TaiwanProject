import sys
q = sys.stdin.read()
q1 = q.splitlines()
for i in range(1, len(q1)):
    q2 = q1[i].split()
    print(len(q2))
