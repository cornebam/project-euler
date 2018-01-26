summe = 0
temp_sum = 0
for i in range(2, 1000000):
	
	for k in range(len(str(i))):
		temp_sum += int(str(i)[k])**5
	
	if i == temp_sum:	
		summe += i
		print(i)
	
	temp_sum = 0

print(summe)
	
