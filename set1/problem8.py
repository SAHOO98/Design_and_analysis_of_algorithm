def OddOrEven(x):
    if x==1: return 1
    elif x==2: return 0
    else: return OddOrEven(x-2)

if __name__ ==  "__main__":
	print(OddOrEven(8))