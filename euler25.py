fibo = [0,1]
i = 1
count = 2
while(len(str(i)) < 1000):
	i = fibo[count - 2] + fibo[count - 1]
	fibo.append(i)
	count += 1

print(fibo.index(i))
