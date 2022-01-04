import db_stuff
import unittest

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
		self.assertFalse(db_stuff.CheckPassword("aaaaaaa")) # bad size no MAJ no Special
		self.assertFalse(db_stuff.CheckPassword("aAaa#aa")) # bad size MAJ Special
		self.assertFalse(db_stuff.CheckPassword("aaaaaaaa")) # good size no MAJ no Special
		self.assertFalse(db_stuff.CheckPassword("aaaaAaaa")) # good size MAJ no Special
		self.assertFalse(db_stuff.CheckPassword("aaaa#aaa")) # good size no MAJ Special
		self.assertTrue(db_stuff.CheckPassword("aAaa#aaa")) # good size MAJ Special


if __name__ == '__main__':
	unittest.main()
