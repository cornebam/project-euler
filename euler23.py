def get_factor_sum(number):
    summe = 0
    for x in range(1,number):
        if number % x == 0:
            summe += x
    return summe

abundants = []
temp_number = 0
   
def sum_check(number):
    for i in abundants:
        if i > number:
            return number
        temp_number = number - i
        if temp_number in abundants:
            return 0
        
"""
    for i in abundants:
        if i > number:
            break
        for j in abundants:
            if i + j == number:
                return 0
            if i + j > number:
                break
    return number
"""

for i in range(1,28124):
    if  get_factor_sum(i) > i:
        abundants.append(i)
        
solution = 0
#print abundants

for k in range(1,28124):
    #print k
    solution += sum_check(k)
print solution