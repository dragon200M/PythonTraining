#!/usr/bin/python3.5

import unittest
from prime import *

class isPrimeTest(unittest.TestCase):

    def testOne(self):
        self.assertEquals(is_prime(0), False,"0 is not a prime")

    def testTwo(self):
        self.assertEquals(is_prime(1), False,"1 is not a prime")

    def testThree(self):
        self.assertEquals(is_prime(2), True,"2 is a prime")

    def testThree(self):
        self.assertEquals(is_prime(-1), False,"-1 is not a prime")

    def testThree(self):
        self.assertEquals(is_prime(73), True,"73 is  a prime")

    def testThree(self):
        self.assertEquals(is_prime(9), False ,"9 is  not a prime")


def main():
    unittest.main()

if __name__ == '__main__':
    main()

