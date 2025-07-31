def NWD(a, b):
	while a != b:
		if a > b:
			a = a - b
		else:
			b = b - a
	return a
    
def NWW(a, b):
	return a * b // NWD(a, b)
    
def czy_wzglednie_pierwsze(a, b):
	return NWD(a, b) == 1