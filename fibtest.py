a,b,n = 0,1,10

while n:
	yield b
	a,b = b,a+b
	n = n - 1

