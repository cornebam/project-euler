zahlen = {0:0,1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4,10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8,20:6,30:6,40:5,50:5,60:5,70:7,80:6,90:6,100:7,1000:8}
summe = 0
for x in range(1001):
    x = str(x)
    while len(x) < 4:
        x = "0" + x
    print(x)
    for i in range(4):
        print(summe)
        if i == 0 and x[i] != "0":
            summe += zahlen[1000] + zahlen[1]
        if i == 1 and x[i] != "0":
            summe += zahlen[100] + zahlen[int(x[i])]
            if x[i+1] != "0" or x[i+2] != "0":
                summe += 3
        if i == 2 and x[i] != "0":
            if int(x[i]) < 2:
                if int(x[i+1]) == 0:
                    summe += zahlen[10]
                    break
                a = x[i]+x[i+1]
                summe += zahlen[int(a)]
                break
            else:
                summe += zahlen[int(x[i])*10]
        if i == 3 and x[i] != "0":
            summe += zahlen[int(x[i])]

print(summe)

y = 0
for k in range(20):
    y += zahlen[k]
print(y)
 