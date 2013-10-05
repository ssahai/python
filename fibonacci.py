# To print fibonacci numbers upto a given range

range = int (raw_input ("Enter the range for the series : "))
i = 0
j = 1
k = 0
while i < range:
    print i
    k = i + j
    i = j
    j = k
