def factorial(n):
    global f
    if n == 0:
        return int(1)
    f = n * factorial(n-1)
    return f

n = int(raw_input ("Enter Number : "))
f=1
fact = factorial (n)
print "Factorial of %d is : %d" % (n, fact)
