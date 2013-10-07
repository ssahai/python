t = int (raw_input ())
out = []
for i in range (0, t):
    str = raw_input()
    c = 0
    for char in str:
        if char == 'A' or char == 'D' or char == 'O' or char == 'P' or char == 'Q' or char == 'R':
            c = c + 1
        elif char == 'B':
            c = c + 2
    out.append(c)

for i in range (0, t):
    print out[i]
            
