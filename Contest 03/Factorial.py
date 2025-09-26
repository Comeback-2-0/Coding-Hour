"""
You are given a positive integer n. Your task is to calculate the factorial of n
using a loop. The factorial of a number n is defined as: n!=1×2×3×⋯×n 
Note: The factorial of 0 is 1.


Test cases:
1) input : 1    output: 1 
2) input : 3    output: 6
3) input : 0    output: 1
4) input : 5    output: 120
5) input : 7    output: 5040

"""

n = int(input())
fact = 1
for i in range(1, n + 1):
    fact *= i

print(fact)