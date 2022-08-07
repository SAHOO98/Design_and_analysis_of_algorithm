def is_Valid(x):
	if x==1 or x==2:
		return True
	elif x<1:
		return False
	else:
		if x%2 ==1 :
			return is_Valid(x-3)
		else:
			return is_Valid(x-3) or is_Valid(x/2)

if __name__ == "__main__":
	a = [262, 646, 800, 61, 44]
	for x in a:
		print(is_Valid(x))
