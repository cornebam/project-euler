import sympy

primes = []

for i in range(2,10000):
	print(i)
	if sympy.isprime(i):
		primes.append(i)

combinations = []

for a in range(-999, 999):
	print(a)
	for b in range(-1000, 1000):
		for n in range(100):
			x = n*n+a*n+b
			if x < 1:
				combinations.append([n-1, a, b])
				break
			if x not in primes:
				combinations.append([n-1, a, b])
				break

combinations.sort()
print(combinations[len(combinations)-1][1] , combinations[len(combinations)-1][2])
