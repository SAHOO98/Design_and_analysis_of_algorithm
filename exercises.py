import sys

def oddeven(x):
    if x==1: return 1
    elif x==2: return 0
    else: return oddeven(x-2)

def is_valid(a,b):
	if a==0 and b==0: 
		return True
	elif a<0 or b<0:
		return False
	else: 
		return is_valid(a,b-1) or is_valid(a-1,b-1) or is_valid(a-2, b-1)

def is_Valid(x):
    if x == 1 and x==2:
        return True
    elif x<1:
        return False
    else:
        if x%2==1:
            return is_Valid(x-3)
        else:
            return is_Valid(x-3) or is_Valid(x/2)

# print(oddeven(int(sys.argv[1])))
# print(is_Valid(int(sys.argv[1])))
print(is_valid(int(sys.argv[1]),int(sys.argv[2])))
