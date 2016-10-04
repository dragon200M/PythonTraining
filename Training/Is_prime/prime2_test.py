#!/usr/bin/python3.5

import unittest
from prime import is_prime2

class isPrime2Test(unittest.TestCase):

    def testOne(self):
        self.assertEquals(is_prime2(0), False,"0 is not a prime")

    def testTwo(self):
        self.assertEquals(is_prime2(1), False,"1 is not a prime")

    def testThree(self):
        self.assertEquals(is_prime2(2), True,"2 is a prime")

    def testFour(self):
        self.assertEquals(is_prime2(-1), False,"-1 is not a prime")

    def testFive(self):
        self.assertEquals(is_prime2(73), True,"73 is  a prime")

    def testSix(self):
        self.assertEquals(is_prime2(9), False ,"9 is  not a prime")

def main():
    unittest.main()

if __name__ == '__main__':
    main()