#!/usr/bin/python3.5


def solution(number):
    s= 0

    for i in range(number):
        if i%3 == 0 or i%5 == 0:
            s+=i

    return s


def solution2(number):
    s=0
    s = sum([n for n in range(number) if n % 3 == 0 or n % 5 == 0])

    return  s