fibonacci = [1,2]
summe = 2
for x in range(1000000):
     number = fibonacci[len(fibonacci)-1] + fibonacci[len(fibonacci)-2]
     if number > 4000000:
         break
     fibonacci.append(number)
     if number % 2 == 0:
         summe += number
print summe