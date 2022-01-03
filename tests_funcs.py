import funcs
import unittest
import random
import math

EMPTY_LIST=0
ZERO_LIST=1
SINGLE_NEG=2
SINGLE_POS=3
ORDERED_POS=4
RAND_POS=5
ORDERED_POS_NEG=6
RAND_POS_NEG=7
ORDERED_NEG=8
RAND_NEG=9

class TestFuncs(unittest.TestCase):

	test_int_list = [
				[], # EMPTY_LIST
				[ 0 ], # ZERO_LIST
				[ -2 ], # SINGLE_NEG
				[ 2 ], # SINGLE_POS
				[ 0, 1, 2, 3, 4, 5, 10], # ORDERED_POS
				[10, 0, 5, 2, 4, 1, 3], # RAND_POS
				[ -5, -2, 0, 1, 2, 3, 4, 5, 10], # ORDERED_POS_NEG
				[3, 2, 5, -2, 4, -5, 10, 0, 1], # RAND_POS_NEG
				[-10, -5, -4, -3, -2, -1, 0], # ORDERED_NEG
				[-1, -4, -2, -3, -5, 0, -10] # RAND_NEG
			]

	def test_max_int(self):
		self.assertEqual(funcs.max_int(0,2),2)
		self.assertEqual(funcs.max_int(-1,-5),-1)
		self.assertEqual(funcs.max_int(-1,2),2)
		self.assertEqual(funcs.max_int(0,0),0)

	def test_average(self):
		self.assertEqual(funcs.average(self.test_int_list[EMPTY_LIST]),None)
		self.assertEqual(funcs.average(self.test_int_list[ZERO_LIST]),0)
		self.assertEqual(funcs.average(self.test_int_list[SINGLE_NEG]),-2)
		self.assertEqual(funcs.average(self.test_int_list[SINGLE_POS]),2)
		# first problem : how to compare floats? easiest way :
		# math.isclose(a, b, abs_tol=0.0001)
		self.assertTrue(math.isclose(
						funcs.average(self.test_int_list[ORDERED_POS]),
						3,5714,
						0.001
					)
			)
		self.assertTrue(math.isclose(
						funcs.average(self.test_int_list[RAND_POS]),
						3,5714,
						0.001
					)
			)
		self.assertEqual(funcs.average(self.test_int_list[ORDERED_POS_NEG]),2)
		self.assertEqual(funcs.average(self.test_int_list[RAND_POS_NEG]),2)
		self.assertTrue(math.isclose(
						funcs.average(self.test_int_list[ORDERED_NEG]),
						-3,5714,
						0.001
					)
			)
		self.assertTrue(math.isclose(
						funcs.average(self.test_int_list[RAND_NEG]),
						-3,5714,
						0.001
					)
			)


if __name__ == '__main__':
	unittest.main()
