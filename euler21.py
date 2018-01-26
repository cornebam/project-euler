def factor_sum(number):
    summe = 0
    for x in range(1,number):
        if number % x == 0:
            summe += x
    return summe

amic_summe = 0
for i in range(1,10000):
    if factor_sum(factor_sum(i)) == i and factor_sum(i) != i:
        print i
        amic_summe += i
print(amic_summe)
