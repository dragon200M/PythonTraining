#!/usr/bin/python3.5


def is_prime(num):
    if num > 0:
        if num == 2:
            return True
        elif num == 1:
            return False
        else:

            for i in range(2,num):
                if(num % i == 0):
                    return False


            return True
    else:
        return False




print(is_prime(9))