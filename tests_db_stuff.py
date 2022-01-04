import db_stuff
import unittest
import string
import random

class TestFuncs(unittest.TestCase):

	def test_CheckUsername(self):
		self.assertFalse(db_stuff.CheckUsername("")) # empty
		self.assertFalse(db_stuff.CheckUsername("aaa")) # bad size
		self.assertFalse(db_stuff.CheckUsername("aaa#")) # good size but special
		self.assertTrue(db_stuff.CheckUsername("aaaaa")) # good size
		self.assertTrue(db_stuff.CheckUsername("aaaa9a")) # good size with number
		self.assertTrue(db_stuff.CheckUsername("aaAa9")) # good size with number and MAJ

	def test_CheckPassword(self):
		self.assertFalse(db_stuff.CheckPassword("")) # empty
		self.assertTrue(db_stuff.CheckPassword("aAaa#a9aa")) # good size MAJ Special number

		self.assertFalse(db_stuff.CheckPassword("aAaa#a9")) # bad size MAJ Special number
		self.assertFalse(db_stuff.CheckPassword("aaaa#a9aa")) # good size no MAJ Special number
		self.assertFalse(db_stuff.CheckPassword("aAaaaa9aa")) # good size MAJ no Special number
		self.assertFalse(db_stuff.CheckPassword("aAaa#aaaa")) # good size MAJ Special no number

	def test_CheckKey(self):
		self.assertTrue(
			db_stuff.CheckKey(
				"".join(random.choices(string.ascii_letters + string.digits + string.punctuation, k = 128))
			) # terrible code to generate a random string
		)
		self.assertFalse(
			db_stuff.CheckKey(
				"".join(random.choices(string.ascii_letters + string.digits + string.punctuation, k = 127))
			) # terrible code to generate a random string
		)
		self.assertFalse(db_stuff.CheckKey(""))


if __name__ == '__main__':
	unittest.main()
