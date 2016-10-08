#!/usr/bin/python3.5

import unittest
from check import *

class checkTest(unittest.TestCase):

    def testOne(self):
        self.assertEquals(group_check("()"), True)
    def testTwo(self):
        self.assertEquals(group_check("({"), False)
    def testThree(self):
        self.assertEquals(group_check("([]"), False)
    def testFour(self):
        self.assertEquals(group_check("{(})"), False)



def main():
    unittest.main()

if __name__ == '__main__':
    main()