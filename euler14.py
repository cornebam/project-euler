numbers = []
for number in range(1,999999):
    cnt = 0
    print(number)
    temp_number = number
    while temp_number != 1:
        #print(temp_number)
        if temp_number % 2 == 0:
            temp_number = temp_number/2
            cnt += 1
        else:
            temp_number = 3*temp_number + 1
            cnt +=1
    numbers.append([number, cnt])
#print(numbers)
solution = [0,0]
for line in numbers:
    if line[1] > solution[1]:
        solution = line
#        print(line)
print(solution)