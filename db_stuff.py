def CheckUsername(username):
	if len(username) <= 3 :
		return False

	for ch in username :
		if not ch.isalnum() :
			return False

	return True

def CheckPassword(password):
	return False
