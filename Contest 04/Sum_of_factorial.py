"""

Given a positive integer N, write a program to calculate the sum of the factorials of its digits.

For example, if the number is 145, then the sum of the factorials of its digits is: 
1! + 4! + 5! = 1 + 24 + 120 = 145

Test cases:
Test Case 0: input: 1  output: 1
Test Case 1: input: 105  output: 122
Test Case 2: input: 145  output: 145
Test Case 3: input: 100  output: 3
Test Case 4: input: 222  output: 6


"""

N = int(input())

sum_factorials = 0
temp = N

while temp > 0:
    digit = temp % 10
    
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
    
    sum_factorials += fact
    temp //= 10

print(sum_factorials)