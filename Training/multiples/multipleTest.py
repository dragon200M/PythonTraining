#!/usr/bin/python3.5


import unittest
from multiple import *


class multiple(unittest.TestCase):

    def testOne(self):
        self.assertEquals(solution(10), 23)

class multiple2(unittest.TestCase):

    def testOne(self):
        self.assertEquals(solution2(10), 23)


def main():
    unittest.main()

if __name__ == '__main__':
    main()