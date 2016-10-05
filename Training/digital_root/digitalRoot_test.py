#!/usr/bin/python3.5

import unittest
from digitalRoot import *

class digitalRootTest(unittest.TestCase):

    def testOne(self):
        self.assertEquals(digital_root(16), 7)
    def testTwo(self):
        self.assertEquals(digital_root(942), 6)
    def testThree(self):
        self.assertEquals(digital_root(132189), 6)
    def testFour(self):
        self.assertEquals(digital_root(493193), 2)



class digitalRoot2Test(unittest.TestCase):

    def testOne(self):
        self.assertEquals(digital_root2(16), 7)
    def testTwo(self):
        self.assertEquals(digital_root2(942), 6)
    def testThree(self):
        self.assertEquals(digital_root2(132189), 6)
    def testFour(self):
        self.assertEquals(digital_root2(493193), 2)



def main():
    unittest.main()

if __name__ == '__main__':
    main()