counter = 0
for i in range(123456789, 9876543211):
	i = str(i)
	if len(i) == 9:
		i = "0" + i
	if len(set(i)) != 10:
		continue
	else:
		counter += 1
		print(counter)
	if counter == 1000000:
		print(i)
