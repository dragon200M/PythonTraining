#!/usr/bin/python3.5



def is_prime(num):
    if num > 0:
        i=2
        if num == i:
            return True
        elif num == 1:
            return False
        else:

            for i in range(2,num):
                print(i)
                if(num % i == 0):
                    return False
                else:
                    return True

    else:
        return False


print(is_prime(2))

