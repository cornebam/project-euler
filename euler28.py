sum_diag = 1
a = 3
while(a < 1003):
	sum_diag += (a*a + (a*a - (a-1)*2) * 3)
	a += 2
	print(a)
print(sum_diag)
