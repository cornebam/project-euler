import string
count = 0
alphabet = []
for letter in string.ascii_lowercase:
    count += 1
    alphabet.append(letter)
    alphabet.append(count)
i = iter(alphabet)
d = dict(zip(i, i))

f = open("euler22.txt", "r")
for line in f:
    names = line.split(",")
print d
#print names
names = sorted(names)

solution = 0

for name_index in range(len(names)):
    #print  names[name_index].replace('"',"").lower()
    name_sum = 0
    for letter in names[name_index].replace('"',"").lower():
        name_sum += d[letter]

    solution += name_sum * (name_index + 1)

print solution