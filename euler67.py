
f = open("euler67.txt", "r")
temp_numbers = []
pyramid = []
for line in f:
    temp_numbers.append(line.strip())
for element in temp_numbers:
    pyramid.append(element.split(" "))


current_row = 1
current_coloumn = 0
path_sum = int(pyramid[0][0])

for i in range(1, 100):
	print(path_sum)
	if current_row > 100:
		break
	
	if int(pyramid[current_row][current_coloumn]) > int(pyramid[current_row][current_coloumn + 1]):
		path_sum += int(pyramid[current_row][current_coloumn])
	else:
		path_sum += int(pyramid[current_row][current_coloumn + 1])
		current_coloumn += 1
	current_row += 1

print(path_sum)
