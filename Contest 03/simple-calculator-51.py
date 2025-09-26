"""

Write a program that takes two integer numbers and an arithmetic operator (+, -, *, /) as input. Perform the specified operation and print the result. If the operator is not among the valid ones, print "Invalid operator".

Input Format:-

First line contains an integer a
Second line contains an integer b
Third line contains a character representing the operator (+, -, *, /)


Test cases:
1) input : 5 6 +    output: 11
2) input : -9 8 *    output: -72 
3) input : 5 6 **   output: Invalid Operator
4) input : 10 5 /    output: 2.0
5) input : 29 30 -    output: -1

"""

a = int(input())
b = int(input())
op = input()

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    print(a / b)  
else:
    print("Invalid operator")