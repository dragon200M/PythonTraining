#!/usr/bin/python3.5


def square_digits(num):
    a=list(int(digit)*int(digit) for digit in str(num))
    return int("".join(map(str,a)))


