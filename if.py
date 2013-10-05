#!/usr/bin/python
# To check whether the guessed number is correct (as per our fixed number)

num = 15
guess = int (raw_input ("Enter you guess : "))

if guess == num:
    print 'You guessed it right!'
elif guess > num:
    print 'Your guesses a larger number'
else:
    print 'You guessed a smaller number'

print 'Program exits'
