distinct_terms = []

for a in range(2, 101):
	for b in range(2, 101):
		distinct_terms.append(a**b)

		
print(len(set(distinct_terms)))
