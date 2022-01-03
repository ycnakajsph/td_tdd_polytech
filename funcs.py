import math

def max_int(a,b):
	if a < b :
		return b
	else :
		return a

def average(list_int):
	if len(list_int) == 0 :
		return None
	return sum(list_int)/len(list_int)

def median(list_int):
	if len(list_int) == 0 :
		return None
	if len(list_int) == 1 :
		return list_int[0]
	list_int.sort()
	len_list = len(list_int)
	ind = (len_list - 1) // 2

	if len_list%2 :
		return list_int[ind]
	else :
		return (list_int[ind]+list_int[ind+1])/2.0


def stddev(list_int):
	if len(list_int) == 0 :
		return None
	av = average(list_int)
	dev = 0
	for item in list_int :
		dev = dev + (item-av)*(item-av)

	return math.sqrt(dev/len(list_int))
