# Script to test the primality of the number using trial division method

num = long (raw_input ("Enter to number to be checked :"))
flag = True

for i in range (2, num-1):
    if num % i == 0:
        print 'Number is COMPOSITE, and the smallest factor is %d' % i
        flag = False
        break

if flag:
    print ' The number is PRIME'
