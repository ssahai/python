t = int (raw_input ())
f = []
for i in range (0, t):
    n = int (raw_input ())
    fact = 1
    for j in range (1, n+1):
        fact = fact * j
    f.append(fact)
for i in range (0, t):
    print f[i]
