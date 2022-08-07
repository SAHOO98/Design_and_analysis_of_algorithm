def foo(a,b):
	if a==1 and b==2:
		return True
	elif a>b:
		return False
	else:
		return foo(b-a,a)

if __name__ ==  "__main__":
	print(foo(2584, 4181))

