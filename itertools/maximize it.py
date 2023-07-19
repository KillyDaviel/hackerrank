from itertools import product as pr
a=input().split()
K=int(a[0])
M=int(a[1])

N=[]
for i in range (K):
    lst=list(map(int,input().split()))
    del(lst[0])
    # lst=lst[1:len(lst)]
    N.append(lst)

pro=list(pr(*N))

fin=0
for item in pro:
    sum=0
    for num in item: 
        sum+= num**2
    mod = sum % M
    if (mod>fin):
        fin = mod        
print(fin)

'''Question: Maximize it [Python Itertools,]
You are given a function f(X) = X2. You are also given K lists. The ith list consists of Ni elements.
You have to pick one element from each list so that the value from the equation below is maximized:
S = (f(X1) + f(X2) +....+ f(Xk)) % M
Xi denotes the element picked from the ith list. Find the maximized value Smax obtained.
% denotes the modulo operator.

Note that you need to take exactly one element from each list, not necessarily the largest element.
You add the squares of the chosen elements and perform the modulo operation. The maximum value that
you can obtain, will be the answer to the problem.

Input Format:

The first line contains 2 space-separated integers K and M.
The next K lines each contain an integer Ni, denoting the number of elements in the ith list, 
followed by Ni space-separated integers denoting the elements in the list.

Constraints:

1 <= K <= 7
1 <= M <= 1000
1 <= Ni <= 7
1 <= Magnitude of elements in list <= 109

Output Format:

Output a single integer denoting the value Smax.

Sample Input:

bash

3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 
Sample output:

bash

206'''