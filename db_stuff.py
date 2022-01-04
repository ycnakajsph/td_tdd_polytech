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
	return True

