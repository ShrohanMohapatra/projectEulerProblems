# ProjectEulerProblem44.py

last10Digs = 0
numOfDigs = 10
for k in range(1, 1001):
	last10Digs = last10Digs + ((k**k) % 10**numOfDigs)

last10Digs = last10Digs % 10**numOfDigs

print(last10Digs)
