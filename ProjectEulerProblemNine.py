# ProjectEulerProblemNine.py

import math

targNum = 1000
nMax = targNum//2

for k in range(2, nMax):
	if 500 % k == 0:
		m = (math.floor(math.sqrt(1 + 4*500//k)) - 1)//2
		a = 2*k*m
		b = k*(m**2-1)
		c = k*(m**2+1)
		targetExpr = math.floor(math.fabs(a+b+c-1000))
		assert(math.floor(math.fabs(a**2+b**2-c**2)) == 0)
		if targetExpr == 0: break
assert(a == 200)
assert(b == 375)
assert(c == 425)
assert(a*b*c == 31875000)

