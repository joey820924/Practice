def sqrt(x):
	r = x
	while(r*r>x):
		r = (r+x/r)/2
	return r*r==x

print(sqrt(17))