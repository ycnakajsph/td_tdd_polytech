import db_stuff
import unittest
import string
import random
import sqlite3

class TestFuncs(unittest.TestCase):

	test_db = "test_db.db"

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

	def test_CreateDb(self):
		self.assertTrue(db_stuff.CreateDb(self.test_db))
		# Let's check that the created db has all necessary tables and fields

		con = sqlite3.connect(self.test_db)
		cursor = con.execute('select * from USERS')
		names = list(map(lambda x: x[0], cursor.description))
		self.assertIn("username",names)
		self.assertIn("password",names)
		self.assertIn("spublickey",names)
		self.assertIn("sprivatekey",names)
		self.assertIn("epublickey",names)
		self.assertIn("eprivatekey",names)


if __name__ == '__main__':
	unittest.main()
