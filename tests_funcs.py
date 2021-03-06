import funcs
import unittest
import random

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
ORDERED_POS_NEG_SIZE_PAIR=10
TWO_POS_LIST=11

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
				[-1, -4, -2, -3, -5, 0, -10], # RAND_NEG
				[ -5, -2, 0, 1, 2, 3, 4, 5], # ORDERED_POS_NEG_SIZE_PAIR
				[ 1, 2] # TWO_POS_LIST
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
		# self.assertAlmostEqual(a,b,places=<n decimals> )
		self.assertAlmostEqual(
						funcs.average(self.test_int_list[ORDERED_POS]),
						3.5714,
						places=3
					)

		self.assertAlmostEqual(
						funcs.average(self.test_int_list[RAND_POS]),
						3.5714,
						places=3
					)

		self.assertEqual(funcs.average(self.test_int_list[ORDERED_POS_NEG]),2)
		self.assertEqual(funcs.average(self.test_int_list[RAND_POS_NEG]),2)
		self.assertAlmostEqual(
						funcs.average(self.test_int_list[ORDERED_NEG]),
						-3.5714,
						places=3
					)

		self.assertAlmostEqual(
						funcs.average(self.test_int_list[RAND_NEG]),
						-3.5714,
						places=3
					)


	def test_median(self):
		self.assertEqual(funcs.median(self.test_int_list[EMPTY_LIST]),None)
		self.assertEqual(funcs.median(self.test_int_list[ZERO_LIST]),0)
		self.assertEqual(funcs.median(self.test_int_list[SINGLE_POS]),2)
		self.assertEqual(funcs.median(self.test_int_list[SINGLE_NEG]),-2)
		self.assertEqual(funcs.median(self.test_int_list[ORDERED_POS]),3)
		self.assertEqual(funcs.median(self.test_int_list[RAND_POS]),3)
		self.assertEqual(funcs.median(self.test_int_list[ORDERED_POS_NEG]),2)
		self.assertEqual(funcs.median(self.test_int_list[RAND_POS_NEG]),2)
		self.assertEqual(funcs.median(self.test_int_list[ORDERED_NEG]),-3)
		self.assertEqual(funcs.median(self.test_int_list[RAND_NEG]),-3)
		self.assertEqual(funcs.median(self.test_int_list[ORDERED_POS_NEG_SIZE_PAIR]),1.5)
		self.assertEqual(funcs.median(self.test_int_list[TWO_POS_LIST]),1.5)

	def test_stddev(self):
		self.assertEqual(funcs.stddev(self.test_int_list[EMPTY_LIST]),None)
		self.assertEqual(funcs.stddev(self.test_int_list[ZERO_LIST]),0)
		self.assertEqual(funcs.stddev(self.test_int_list[SINGLE_POS]),0)
		self.assertEqual(funcs.stddev(self.test_int_list[SINGLE_NEG]),0)
		self.assertAlmostEqual(funcs.stddev(self.test_int_list[ORDERED_POS]),3.0639,places=3)
		self.assertAlmostEqual(funcs.stddev(self.test_int_list[RAND_POS]),3.0639,places=3)
		self.assertAlmostEqual(funcs.stddev(self.test_int_list[ORDERED_POS_NEG]),4.0551,places=3)
		self.assertAlmostEqual(funcs.stddev(self.test_int_list[RAND_POS_NEG]),4.0551,places=3)
		self.assertAlmostEqual(funcs.stddev(self.test_int_list[ORDERED_NEG]),3.0639,places=3)
		self.assertAlmostEqual(funcs.stddev(self.test_int_list[RAND_NEG]),3.0639,places=3)
		self.assertAlmostEqual(funcs.stddev(self.test_int_list[ORDERED_POS_NEG_SIZE_PAIR]),3.0822,places=3)
		self.assertEqual(funcs.stddev(self.test_int_list[TWO_POS_LIST]),0.5)

	def test_is_geoprog(self):
		self.assertFalse(funcs.is_geoprog([]))
		self.assertFalse(funcs.is_geoprog([0]))
		self.assertTrue(funcs.is_geoprog([2,6,18,54])) # u0 = 2 , r = 3
		self.assertTrue(funcs.is_geoprog([2,-6,18,-54])) # u0 = 2 , r = -3
		self.assertTrue(funcs.is_geoprog([-2,6,-18,54])) # u0 = -2 , r = -3
		self.assertFalse(funcs.is_geoprog([-2,6,18,54])) # third item wrong
		self.assertFalse(funcs.is_geoprog([-2,6,-18,54,162])) # last item wrong

	def test_get_nnextgeoprog(self):
		self.assertEqual(funcs.get_nnextgeoprog(2,[]),(False,None)) # one edge case
		self.assertEqual(funcs.get_nnextgeoprog(2,[2,-6,18,-54]),(True, [162,-486])) # one good prog
		self.assertEqual(funcs.get_nnextgeoprog(2,[-2,6,18,54]),(False,None)) # one wrong prog
		self.assertEqual(funcs.get_nnextgeoprog(0,[-2,6,-18,54]),(True,None)) # in case we ask for 0 elem ret True None with true prog
		self.assertEqual(funcs.get_nnextgeoprog(0,[-2,6,18,54]),(False,None)) # in case we ask for 0 elem ret False None with false prog

if __name__ == '__main__':
	unittest.main()
