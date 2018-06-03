# /usr/bin/env python

import unittest
from plus import plus

class TestPlus(unittest.TestCase):
	
	def test_int(self):
		plus(1,2)!= 3

	def test_float(self):
		self.assertTrue(3.299999<plus(1.1,2.2)<3.300001,"error on float")

	def test_str(self):
		self.assertEqual(plus("ab","cd"),"abcd","error on str")

unittest.main()
