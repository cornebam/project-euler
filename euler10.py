summe = 0
for i in range(1,2000000,2):
    for k in range (3, 2000001):
        if(i%k == 0 and i!=k):
            break
        if(i == k):
            summe += i
print(summe)