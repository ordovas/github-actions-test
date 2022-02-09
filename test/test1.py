# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 11:09:35 2022

@author: 940700
"""

import unittest


def dummy_sum(a,b):
    return a+b
"""
def readtxt_fun(input_path: str):
    with open(input_path) as f:
        lines = f.read()
    return lines
"""





class TestSum(unittest.TestCase):
    
    
    def test_veamos1(self):
        z1=2
        z2=3
        self.assertEqual(dummy_sum(z1, z2), 5, "Should be 6")

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_wrong(self):
        self.assertEqual(sum((1, 2, 2)), 5, "Should be 5")

if __name__ == '__main__':
    unittest.main()
