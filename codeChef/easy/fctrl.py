import math
t = int (raw_input ())
n = []
for i in range (t):
    n.append(int (raw_input ()))

for i in range (t):
    z = 0
    flag = True
    temp = 5
    p = 1
    while flag:
        c = int (math.floor (n[i] / temp))
        
        if c == 0:
            flag = False
            continue
        else:
            p = p+1
        
        z = z + c
        temp = math.pow (5, p)
    print z

