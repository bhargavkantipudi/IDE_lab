"""
Given an integer, return True if it a Prime number otherwise return False.

Example 1
Input
n = 2

Output
True

"""


import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def is_prime(n):
    if(n==0 or n==1):
        return False
    for x in range(2,n-1):  
        if (n % x) == 0:   
            return False
    else:              
        return True


# DO NOT TOUCH THE BELOW CODE
class TestIsPrime(unittest.TestCase):

    def test_01(self):
        self.assertEqual(is_prime(3), True)

    def test_02(self):
        self.assertEqual(is_prime(12), False)

    def test_03(self):
        self.assertEqual(is_prime(33), False)


if __name__ == '__main__':
    unittest.main(verbosity=2)
