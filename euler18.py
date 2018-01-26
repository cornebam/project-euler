f = open("euler18.txt", "r")
temp_numbers = []
numbers = []
for line in f:
    temp_numbers.append(line.strip())
for element in temp_numbers:
    numbers.append(element.split(" "))
#print(numbers)


temp_numbers = numbers[len(numbers)-1]

#print(temp_numbers)
for row in range(len(numbers)-1, 0, -1):
    exponent = len(numbers) - row
    #print(row)
    #print(numbers[row])
    count = -1
    path_count = len(temp_numbers)
    #print(temp_numbers)
    
    for x in numbers[row - 1]:
        count += 1
        for exp in range(2**exponent):
            temp_numbers.append(int(temp_numbers[exp + count * (2**exponent)/2]) + int(numbers[row-1][count]))
            #print(temp_numbers[exp + count*2**exponent])
    #print(temp_numbers)
    temp_numbers = temp_numbers[path_count:]
    print(temp_numbers)
#print(temp_numbers)
#print(len(temp_numbers))
summe = 0
for x in temp_numbers:
    if x > summe:
        summe = x
print(summe)