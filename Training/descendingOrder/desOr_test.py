#!/usr/bin/python3.5

import unittest
from desOr import *


class desOrTest(unittest.TestCase):

    def testOne(self):
        self.assertEquals(Descending_Order(342), 432)

    def testTwo(self):
        self.assertEquals(Descending_Order2(342), 432)

    def testThree(self):
        self.assertEquals(Descending_Order3(342), 432)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
