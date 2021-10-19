from math import sqrt
def Divisors(n) : 
    i , sum = 1 , 0
    for i in range(1,n):
        if n%i == 0:
            sum += i
    return sum == n
    
print(list(filter(Divisors , range(1,5001))))