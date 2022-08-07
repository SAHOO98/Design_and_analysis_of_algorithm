def OddOrEven (x):
    if x==1:
        return 1
    elif x==2:
        return 0
    else:
        return 1-OddOrEven(x-1)

if __name__ ==  "__main__":
	print(OddOrEven (979))