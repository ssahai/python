#!/usr/bin/python

# To let the user guess the number already stored in code, and output the number of attempts taken

num = 15
running = True
c = 0

while running:
    guess = int (raw_input ("Enter you guess : "))
    c = c+1
    if guess == num:
        print 'You guessed it right!'
        running = False
    elif guess > num:
        print 'Your guesses a larger number'
    else:
        print 'You guessed a smaller number'

print 'You guessed the number correctly in %d turns' % c
