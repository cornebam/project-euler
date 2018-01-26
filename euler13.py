f = open("euler13.txt", "r")
numbers = []
for line in f:
    numbers.append(line.strip())

summe = 0 
for x in numbers:
    summe += int(x)
    
summe = str(summe)
print(summe[:10])
