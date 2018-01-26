fakultaet = 1
summe = 0
for x in range(1,101):
    fakultaet *= x

fakultaet = str(fakultaet)
for y in fakultaet:
    summe += int(y)
print(summe)