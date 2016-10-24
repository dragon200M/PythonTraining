#!/usr/bin/python3.5


import unittest
from nth import *



class nthTest(unittest.TestCase):

    def testOne(self):

        self.assertEquals(delete_nth([20,37,20,21], 1), [20,37,21])

    def testTwo(self):
        
        self.assertEquals(delete_nth([1,1,3,3,7,2,2,2,2], 3), [1, 1, 3, 3, 7, 2, 2, 2])

def main():
    unittest.main()

if __name__ == '__main__':
    main()