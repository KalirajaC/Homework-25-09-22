#random number divisible by given input
import random as r
n=int(input("Enter n : "))
for i in range(n):
    print(r.randrange(0,100,n))