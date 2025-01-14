a=int(input())
b=int(input())
m=int(input())
print(pow(a,b))
print(pow(a,b,m))

'''Task
You are given three integers: a, b, m and . Print two lines.
On the first line, print the result of pow(a,b). On the second line, print the result of pow(a,b,m).

Input Format
The first line contains a , the second line contains b, and the third line contains m.

Constraints

Sample Input

3
4
5
Sample Output

81
1'''

'''
Powers or exponents in Python can be calculated using the built-in power function. Call the power function a^b as shown below:

>>> pow(a,b) 
or

>>> a**b
It's also possible to calculate a^b mod m.

>>> pow(a,b,m)  
This is very helpful in computations where you have to print the resultant % mod.

Note: Here, a and a can be floats or negatives, but, if a third argument is present,  cannot be negative.
     OR if a third argument is given both a and b have to integer 

Note: Python has a math module that has its own pow(). It takes two arguments and returns a float. It is uncommon to use math.pow().'''