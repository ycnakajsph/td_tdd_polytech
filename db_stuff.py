import sqlite3
import os

def CheckUsername(username):
	if len(username) <= 3 :
		return False

	for ch in username :
		if not ch.isalnum() :
			return False

	return True

def CheckPassword(password):
	if len(password) < 8:
		return False

	has_spec_char = False
	has_number = False
	has_upper = False
	has_lower = False
	for ch in password :
		if not ch.isalnum() :
			has_spec_char = True
		if ch.isnumeric() :
			has_number = True
		if ch.isupper() :
			has_upper = True
		if ch.islower():
			has_lower = True

	return has_spec_char and has_number and has_upper and has_lower

def CheckKey(key):
	if len(key) != 128:
		return False
	return True

def CreateDb(db_path):
	# check if file exists if it does return False
	if os.path.isfile(db_path):
		return False
	con = sqlite3.connect(db_path)
	cur = con.cursor()
	cur.execute('''CREATE TABLE users
			(username TEXT NOT NULL UNIQUE ,
			password TEXT NOT NULL,
			spublickey TEXT NOT NULL,
			sprivatekey TEXT NOT NULL,
			epublickey TEXT NOT NULL,
			eprivatekey TEXT NOT NULL
			)''')
	con.commit()
	con.close()
	return True

def AddUser(db_path,username,password,spublickey,sprivatekey,epublickey,eprivatekey):
	if any ([not CheckUsername(username) , not CheckPassword(password),
		not CheckKey(spublickey) , not CheckKey(sprivatekey),
		not CheckKey(epublickey) , not CheckKey(eprivatekey) ]):
		return False
	con = sqlite3.connect(db_path)
	cur = con.cursor()
	try:
		cur.execute("INSERT INTO users VALUES (?,?,?,?,?,?)",(username,password,spublickey,sprivatekey,epublickey,eprivatekey))
	except sqlite3.IntegrityError: # this means that we failed to insert
		con.close()
		return False
	con.commit()
	con.close()
	return True

def CheckUserLogin(db_path,username,password):
	return False

