import shlex

s = raw_input()
a = int(shlex.split(s)[0])
b = float(shlex.split(s)[1])

if a % 5 !=0:
    print "%.2f" % b
elif a > (b - 0.5):
    print "%.2f" % b
else:
    c = b - a - 0.5
    print "%.2f" % c

