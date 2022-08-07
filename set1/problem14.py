def is_valid(a,b):
	if a==0 and b==0: 
		return True
	elif a<0 or b<0:
		return False
	else: 
		return is_valid(a,b-1) or is_valid(a-1,b-1) or is_valid(a-2, b-1)

if __name__ == '__main__':
    print(is_valid(3,2))
