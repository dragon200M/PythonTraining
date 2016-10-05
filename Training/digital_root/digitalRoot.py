#!/usr/bin/python3.5


def digital_root2(n):
    b = sum(int(digit) for digit in str(n))
    if b < 10:
        return b
    else:
        return digital_root2(b)



def digital_root(n):
    a=0
    for digit in str(n):
        a+=int(digit)
    if a < 10:
        return a
    else:
        return digital_root(a)








#A digital root is the recursive sum of all the digits in a number.
#Given n, take the sum of the digits of n.
#If that value has two digits, continue reducing in this way until a
#single-digit number is produced. This is only applicable to the natural numbers.

#Here's how it works (Ruby example given):

#digital_root(16)
#=> 1 + 6
#=> 7

#digital_root(942)
#=> 9 + 4 + 2
#=> 15 ...
#=> 1 + 5
#=> 6
