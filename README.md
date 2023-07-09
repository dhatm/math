# Repo description

This project contains 3 methods to compute the nth fibonacci number. The derivation for the O(1) method uses several math techniques that I thought were cool and wanted to remember.

1. **fibonacci_formula**
  Description: implements the O(1) formula for the nth fibonacci sequence via the following
  

&emsp;&emsp;$ f(n) = {1 \over {\sqrt{5}} } (p^n - q^n)  $    , for n >= 0


where p and q are:<br><br>
&emsp;&emsp;$ p = { {1+{\sqrt{5}} } \over{2} } $ , $ q = { {1-{\sqrt{5}} } \over{2} } $


this formula can be obtained using the 1-sided Z-transform (see end of this file for derivation)

note: this assumes non-negative n here


2. **fibonacci_recursive**
 Description: implements the fibonacci sequence recursively

3. **fibonacci_iterative**
 Description: implements the fibonacci sequence iteratively


## Running 
To run, call  
```shell
$ python fibonacci.py
```

or, for the unit tests, call
```shell
$ python test_fibonacci.py
```


# Derivation 
Derivation of O(1) formula via 1-sided Z-transform

1. start with f(n+2) = f(n+1) + f(n) and compute the 1-sided Z transform for each term. 

	note: I use the definition from [MIT](https://eecs6302.mit.edu/_static/fall21/extras/siebert8.pdf) and [UC Berkeley](https://inst.eecs.berkeley.edu/~ee120/fa19/LectureNotes/Lecture23.pdf) but I've seen a couple places define it differently for some reason

&emsp;&emsp;&emsp;$f(n) \Rightarrow Zxform \Rightarrow F(z) = Z\{f(n)\} = \sum_{z=0}^\inf f(n)z^{-n} $<br>

&emsp;&emsp;&emsp;$f(n+1) \Rightarrow Zxform \Rightarrow Z\{f(n+1)\} = zZ\{f(n)\} - zf(0) = zF(z) - zf(0) $<br>
&emsp;&emsp;&emsp;(shift the whole time-series over 1 spot and then remove the 0th index since it is a one-sided transform)<br>

&emsp;&emsp;&emsp;$f(n+2) \Rightarrow Zxform \Rightarrow Z\{f(n-2)\} = z^2Z\{f(n)\} - z^2f(0) - zf(1) = z^2F(z) - z^2f(0) - z^1f(1) $<br>
&emsp;&emsp;&emsp;(shift the whole time-series over 2 spots and then remove the 0th & 1st index since it is a one-sided transform)<br>

2. combine above terms<br> <br>
&emsp;&emsp;$ f(n+2) = f(n+1) + f(n) \Rightarrow Zxform \Rightarrow$ <br>
&emsp;&emsp;$ \Rightarrow z^2F(z) - z^2f(0) - zf(1) = zF(z) - zf(0)   +  F(z)$<br>


3. substitute in the fibonacci values f(0)=0 and f(1)=1<br><br>
&emsp;&emsp;$ z^2F(z) - z =  zF(z) +F(z)$<br>


4. reorganize so F(z) is alone<br><br>
&emsp;&emsp;$\Rightarrow F(z)[z^2-z-1] =  z$<br>
&emsp;&emsp;$\Rightarrow F(z) =  {z \over [z^2-z-1]}$<br><br>

5. factor denominator (e.g., using quadratic equation)<br><br>
&emsp;&emsp;$F(z) = {z \cdot {1 \over z - {1 + \sqrt(5) \over 2} } \cdot {1 \over z - {1 - \sqrt(5) \over 2} } }$<br>


6. let
&emsp;&emsp;$ p = { {1+{\sqrt{5}} } \over{2} } $ , $ q = { {1-{\sqrt{5}} } \over{2} }$<br><br>
&emsp;&emsp;$\Rightarrow F(z) = {z  \over (z - p) (z - q) }$<br><br>

7. multiply numerator and denominator by $z^2$<br><br>
&emsp;&emsp;$\Rightarrow F(z) = {z^{-1} \over (1 - pz^{-1}) (1 - qz^{-1})} $ <br>



8. using $x = z^{-1}$ in the above yields (this optional substitution may make it clearer)<br><br>
&emsp;&emsp;$\Rightarrow F(x) = {x \over (1 - px) (1 - qx)} $ <br>


9. separate into 2 fractions via partial fraction expansion to get residuals<br><br>
&emsp;&emsp;$\Rightarrow F(x) = {x \over (1 - px) (1 - qx)} = {A \over 1 - px} + {B \over 1 - qx}$&emsp;&emsp;&emsp;And find A and B<br>
<br>
To find A and B, cross-multiply residuals by (1-px) or (1-qx) and set limit of x to roots.<br>
<br>
&emsp;&emsp;For multiplication with (1-px):<br>
&emsp;&emsp;$\Rightarrow F(x)(1 - px)\rvert_{x=1/p} = {x \over 1-qx}{1 - px\over 1 - px} \rvert_{x=1/p}$<br>
&emsp;&emsp;$\Rightarrow A + B{1 - px\over 1 - qx}\rvert_{x=1/p} = {x \over 1-qx} \rvert_{x=1/p} $<br>
&emsp;&emsp;$\Rightarrow A + B \cdot 0 = {1/p \over {1-q/p} } $<br>
&emsp;&emsp;$\Rightarrow A = {1 \over {p-q}} $<br>
<br>
&emsp;&emsp;And similarily for multiplication with (1-qx)<br>
&emsp;&emsp;$\Rightarrow F(x)(1 - qx)\rvert_{x=1/q} = {x \over 1-px}{1 - qx\over 1 - qx} \rvert_{x=1/q}$<br>
&emsp;&emsp;$\Rightarrow A{1 - qx \over 1 - px}\rvert_{x=1/q} + B = {x \over 1-px} \rvert_{x=1/q} $<br>
&emsp;&emsp;$\Rightarrow 0 + B = {1/q \over {1-p/q} } $<br>
&emsp;&emsp;$\Rightarrow B = {1 \over {q-p}} = -A$
<br>
<br>
from step 6<br>
&emsp;&emsp;$p - q = {1 + \sqrt{5} \over 2} - {1 - \sqrt{5} \over 2} = \sqrt{5}$
<br>
yields<br>
&emsp;&emsp;$A = {1 \over \sqrt{5}}$&emsp;,&emsp;$B = -{1 \over \sqrt{5}} $<br>
<br>
So <br>
&emsp;&emsp;$\Rightarrow F(x) = {1/\sqrt{5} \over 1-px} - {1/\sqrt{5} \over 1-qx} = {1 \over \sqrt{5}}({1 \over 1-px} - {1 \over 1-qx})$<br>


11. returning back to F(z), the above yields<br><br>
&emsp;&emsp;$\Rightarrow F(z) = {1 \over \sqrt{5}}({1 \over 1-pz^{-1}} - {1 \over 1-qz^{-1}}) $<br>


12. taking the inverse 1-sided Z-transform yields<br><br>
&emsp;&emsp;$F(z) \Rightarrow Zxform_{inv} \Rightarrow$<br><br>
&emsp;&emsp;$\Rightarrow f(n) = {1 \over \sqrt{5}}(p^n - q^n)$&emsp;&emsp;for n >= 0, and 0 otherwise<br>
<br>
where p and q were defined in step 6 as<br><br>
&emsp;&emsp;$ p = { {1+{\sqrt{5}} } \over{2} } $ , $ q = { {1-{\sqrt{5}} } \over{2} }$<br><br>

Thus concludes the derivation.




