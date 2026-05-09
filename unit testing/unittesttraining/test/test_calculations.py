import unittest

from src.calculations import add

from src.calculations import sub

from src.calculations import mul

from src.calculations import div

class TestCalculations(unittest.TestCase):
    def test_add(self):
        res=add(10,5)
        self.assertEqual(res,15,msg="addition error")
    def test_sub(self):
        res=sub(10,5)
        self.assertEqual(res,15,msg="multiplication error")
    def test_mul(self):
        res=mul(10,5)
        self.assertEqual(res,50,msg="multiplication error")
    def test_div(self):
        res=div(10,5)
        self.assertEqual(res,2,msg="division error")