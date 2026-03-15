# ProblemEulerProblem20.py

fact = 1
for k in range(1, 101):
	fact = fact * k
stringDigs = str(fact)
print(stringDigs)
print(sum([int(stringDigs[k]) for k in range(len(stringDigs))]))
