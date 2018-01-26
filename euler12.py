# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 04:02:08 2016

@author: cornelius
"""

limit = 10**4
#limit = 50
primes = [x for x in range(0,limit+1)]
primes[0] = 0
primes[1] = 0
for x in range(2, limit):
    if primes[x] != 0:
        for y in range(x, limit/x+1):
            primes[x*y] = 0

primes = filter(lambda x: x != 0, primes)
#print(primes)
divs = []
triang = 0
n = 500
limit = 10**5

for x in range(1, limit):
    triang += x
    cnt = 1
    i = 1
    for prime in primes:
        i = 0
        while True:
            i += 1
            if prime > triang:
                break
            if triang % prime**i == 0:
#                divs.append([triang, prime, i, cnt])
#                print(triang, prime, i, cnt)
                continue
            elif i >= 2:
                cnt *= i
                
                print(triang, prime, i, cnt)
            if cnt >= n:
                print(triang)                
                exit()
            else:
                break
print(triang)