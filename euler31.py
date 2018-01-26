count = 1

for a in range(0, 300, 100):
	for b in range(0, 250, 50):
		for c in range(0, 220, 20):
			for d in range(0, 210, 10):
				for e in range(0, 205, 5):
					for f in range(0, 202, 2):
						for g in range(0, 201):
							if a+b+c+d+e+f+g > 200:
								break
							if a+b+c+d+e+f+g == 200:
								count += 1

print(count)
