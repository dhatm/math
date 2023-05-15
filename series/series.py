#------------------------------------
#imports
from numpy import pi as pi

#------------------------------------
#higher order function helper
def makes_series(f):
    def sums(n):
        cum=0
        while n > 0:
            cum=cum+f(n)
            n=n-1
        return cum
    return sums




#------------------------------------
# various series

print("computing various sums\n")

#1. sum of inverse squares -- converges to pi^2 / 6 (derivable using parseval's theorem)
print("computing sums of squared inverses")
fsuminvsqr=makes_series(lambda x: 1/(x**2))
n=30000000
sn=fsuminvsqr(n)
error=sn - pi**2 /6.  #since series converges to pi^2 / 6
print(f"sum of first {n} squared inverses: {sn}")
print(f"pi^2 /  6: {pi**2 /6.}")
print(f"error sum of inverses: {error}\n")



#2. sum of 1 to n
print("computing sum of first n integers")
fadd=makes_series(lambda x: x)
faddfast=lambda n: n/2*(n+1)
n=100
sn=fadd(n)
error=sn-faddfast(n)
print(f"sum of first {n} integers: {sn}")
print(f"error sum of first n integers: {error}\n")



#3. sum of 1^2 ... to n^2
print("computing sum of first n squared integers")
fsumsqr=makes_series(lambda x: x**2)
fastsumsqr=lambda n: (n * (n + 1) * (2*n + 1)) / 6 
sn=fsumsqr(n)
error=sn-fastsumsqr(n)
print(f"sum of first {n} squared integers: {sn}")
print(f"error sum of first n squared integers: {error}")



