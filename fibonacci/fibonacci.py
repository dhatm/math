###########################################################################
#
# This file contains 3 methods to compute the nth fibonacci number
#
# The derivation for the O(1) method uses several math techniques that I thought were cool and wanted to remember.
#
#
#
###########################################################################


###########################################################################
#  fibonacci_formula
#
#  Description: implements the O(1) formula for the nth fibonacci sequence via the following
#            1      
#  f(n) = ------- * [p^n - q^n] for n >= 0
#         sqrt(5)   
#
#  where p and q are:
#
#        1+sqrt(5)       1-sqrt(5) 
#    p = --------- , q = --------- 
#           2               2      
#
# this formula can be obtained using the 1-sided Z-transform (see end of this file for derivation)
#
def fibonacci_formula(n):
    if n <= 0:
        return 0
    else:
        SQRT5=5**0.5 
        p=(1+SQRT5)/2
        q=(1-SQRT5)/2 #or equivalently q=1-p
        return int(  (p**n - q**n)/SQRT5  )


###########################################################################
# fibonacci_recursive
#
# Description: implements the fibonacci sequence recursively
#
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n <= 1:
        return n 
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

###########################################################################
# fibonacci_iterative
#
# Description: implements the fibonacci sequence iteratively
#
def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n <= 1:
        return n
    else:
        prev1 = 0
        prev2 = 1
        fib = 0

        for i in range(2, n+1):
            fib = prev1 + prev2
            prev1 = prev2
            prev2 = fib

        return fib


###########################################################################
# main 
if __name__ == '__main__':
    print("fibonacci results via 3 methods:")
    print(f"O(1) formula: {fibonacci_formula(10)}")  # output: 55
    print(f"recursion: {fibonacci_recursive(10)}")  # output: 55
    print(f"iterative: {fibonacci_iterative(10)}")  # output: 55



###########################################################################
# derivation of O(1) formula via 1-sided Z-transform (from UC Berkeley EECS 120 techniques)
"""
1. start with f(n+2) = f(n+1) + f(n) and compute the 1-sided Z transform for each term:

  f(n) -> Zxform -> F(z) = Z{f(n)} = sum{n=0 to infinity} f(n)*z^-n
    note: I use the definition from [MIT](https://eecs6302.mit.edu/_static/fall21/extras/siebert8.pdf) and [UC Berkeley](https://inst.eecs.berkeley.edu/~ee120/fa19/LectureNotes/Lecture23.pdf) but I've seen a couple places define it differently for some reason
  
  f(n+1) -> Zxform -> Z{f(n+1)} = z*Z{f(n)} - z*f(0) = z*F(z) - z*f(0)
    (shift the whole time-series over 1 spot and then remove the 0th index since it is a one-sided transform)
  
  f(n+2) -> Zxform -> Z{f(n-2)} = z^2*Z{f(n)} - z^2*f(0) - z*f(1) = z^2*F(z) - z^2*f(0) - z^1*f(1)
    (shift the whole time-series over 2 spots and then remove the 0th & 1st index since it is a one-sided transform)

2. combine terms:
  f(n+2) = f(n+1) + f(n) -> Zxform  ->
  z^2*F(z) - z^2*f(0) - z*f(1) = z*F(z) - z*f(0)    + F(z)

3. substitute in f(0)=0 and f(1)=1 for the fibonacci values:
  z^2*F(z) - z =  z*F(z) +F(z)

4. reorganize so F(z) is alone:
  F(z)*[z^2-z-1] =  z
  F(z) =  z / [z^2-z-1]

5. factor denominator (e.g., using quadratic equation):
                                z
  F(z) =  -------------------------------------------------
          [z - 0.5*(1 + sqrt(5))] * [z - 0.5*(1 - sqrt(5))]


6. let 
        1+sqrt(5)       1-sqrt(5) 
    p = --------- , q = --------- , then
           2               2      
  Then:
                z       
  F(z) =  -------------- 
          [z - p][z - q]

7. multiply numerator and denominator by z^2:
                     z^-1       
  F(z) =  --------------------------- 
          [1 - p*z^-1] * [1 - q*z^-1]

8. using x = z^-1 in the above yields (this optional step may make it clearer):
                   x       
  F(x) =  --------------------- 
          [1 - p*x] * [1 - q*x]

9. separate into 2 fractions via partial fraction expansion to get residuals
                  x                 A                B
  F(x) =  ------------------  = ---------   +   -----------  
          [1 - p*x][1 - q*x]    [1 - p*x]        [1 - q*x]

  find A and B:
     cross-multiply residuals and set limit of x to roots:
         
               x      |            1/p           1        
       A =  --------- |      = -----------  = ------- 
            [1 - q*x] |x=1/p    [1 - q/p]      p - q

               x      |            1/q           1        
       B =  --------- |      = -----------  = ------- = -A
            [1 - p*x] |x=1/q    [1 - p/q]      q - p

     from step #6, p - q = 0.5*[1+sqrt(5)] - 0.5*[1-sqrt(5)] = sqrt(5)

     yields:
       A =  1/sqrt(5)
       B = -1/sqrt(5)

  So 

          1/sqrt(5)      1/sqrt(5)         1         1       1    
  F(x) =  ---------  -  -----------  =  ------- * [----- - ----- ]
          [1 - p*x]      [1 - q*x]      sqrt(5)    1-p*x   1-q*x


11. returning back to F(z), the above yields:
            1          1             1    
  F(z) = ------- * [-------   -  --------]
         sqrt(5)    1-p*z^-1     1-q*z^-1


12. taking the inverse 1-sided Z-transform yields:
  F(z) -> inv Zxform ->
            1      
  f(n) = ------- * [p^n -q^n] for n >= 0, and 0 otherwise
         sqrt(5)   

  where p and q were defined in step #6 as:
        1+sqrt(5)       1-sqrt(5) 
    p = --------- , q = --------- 
           2               2      

"""


