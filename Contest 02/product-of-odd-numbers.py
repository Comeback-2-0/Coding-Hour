"""
At University, the math club organizes a coding challenge where students must work with numbers in a fun way. Instead of just adding numbers, the task is to multiply all the odd numbers up to a given number n.

For example:

- If n = 5, the odd numbers are 1, 3, 5. Their product is 1 × 3 × 5 = 15.

Your task is to calculate the product of all odd numbers from 1 to n using a loop.

**Rules:**

- Input will always be a positive integer n.

- Multiply only the odd numbers between 1 and n (inclusive).

- If n = 1, the product should be 1.

test cases 
1. input : 6 output: 15
2. input : 1 output: 1 
3. input : -7  output: Invalid Input
4. input : 10 output: 945 
5. input : 20 output: 654729075
6. input: 0   output: Invalid Input

"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    product = 1
    for i in range(1, n+1):
        if i % 2 != 0:
            product *= i
    print(product)   



"""
#Solution 2:

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    product = 1
    while n > 0:
        if n % 2 != 0:
            product *= n
        n -= 1
    print(product)
    
"""
    