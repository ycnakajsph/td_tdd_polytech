import unittest
import string
import random
import sqlite3
import os

import db_stuff

class TestFuncs(unittest.TestCase):

	test_db = "test_db.db"

	def setUp(self):
		if os.path.isfile(self.test_db):
			os.remove(self.test_db)
		db_stuff.CreateDb(self.test_db)

	def tearDown(self):
		if os.path.isfile(self.test_db):
			os.remove(self.test_db)

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

	def CreateRandomString(self,n):
		return "".join(random.choices(string.ascii_letters + string.digits + string.punctuation, k = n))

	def test_CheckKey(self):
		self.assertTrue(
			db_stuff.CheckKey(
				self.CreateRandomString(128)
			) # terrible code to generate a random string
		)
		self.assertFalse(
			db_stuff.CheckKey(
				self.CreateRandomString(127)
			) # terrible code to generate a random string
		)
		self.assertFalse(db_stuff.CheckKey(""))

	def test_CreateDb(self):
		if os.path.isfile(self.test_db):
			os.remove(self.test_db)
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

		self.assertFalse(db_stuff.CreateDb(self.test_db)) # verifying we cannot recreate the db

	def test_AddUser(self):
		key = self.CreateRandomString(128) # nobody said anything about using 4 times the same key (yet)
		self.assertFalse(db_stuff.AddUser(self.test_db,"aaa","aAaa#a9aa",key,key,key,key)) # bad username
		self.assertFalse(db_stuff.AddUser(self.test_db,"aaaa","",key,key,key,key)) # bad password
		self.assertFalse(db_stuff.AddUser(self.test_db,"aaaa","aAaa#a9aa",self.CreateRandomString(127),key,key,key)) # bad key
		self.assertFalse(db_stuff.AddUser(self.test_db,"aaaa","aAaa#a9aa",key,self.CreateRandomString(127),key,key)) # bad key
		self.assertFalse(db_stuff.AddUser(self.test_db,"aaaa","aAaa#a9aa",key,key,self.CreateRandomString(127),key)) # bad key
		self.assertFalse(db_stuff.AddUser(self.test_db,"aaaa","aAaa#a9aa",key,key,key,self.CreateRandomString(127))) # bad key
		self.assertTrue(db_stuff.AddUser(self.test_db,"aaaa","aAaa#a9aa",key,key,key,key))
		self.assertFalse(db_stuff.AddUser(self.test_db,"aaaa","aAaa#a9aa",key,key,key,key)) # Not supposed to be able to add 2* same user

	def test_UserLogin(self):
		# Let's add a correct user :
		key = self.CreateRandomString(128)
		self.assertTrue(db_stuff.AddUser(self.test_db,"aaaa","aAaa#a9aa",key,key,key,key))
		self.assertTrue(db_stuff.CheckUserLogin(self.test_db,"aaaa","aAaa#a9aa"))
		self.assertFalse(db_stuff.CheckUserLogin(self.test_db,"aaaa","aAaa#a9a")) # Bad Password
		self.assertFalse(db_stuff.CheckUserLogin(self.test_db,"aaab","aAaa#a9aa")) # Bad Username

	def test_CheckDbHealth(self):
		key = self.CreateRandomString(128)
		self.assertTrue(db_stuff.AddUser(self.test_db,"aaaa","aAaa#a9aa",key,key,key,key))
		key = self.CreateRandomString(128)
		self.assertTrue(db_stuff.AddUser(self.test_db,"bbbb","aAaa#a9aa",key,key,key,key))

		self.assertTrue(db_stuff.CheckDbHealth(self.test_db))

		# Let's add a corrupt User :
		con = sqlite3.connect(self.test_db)
		cur = con.cursor()
		cur.execute("INSERT INTO users VALUES (?,?,?,?,?,?)",
				("#######","aAaa#a9aa",key,key,key,key))
		con.commit()
		con.close()
		self.assertFalse(db_stuff.CheckDbHealth(self.test_db))
		# to be really complete we shall also add tests with bad passwd, bad key and so on

if __name__ == '__main__':
	unittest.main()
