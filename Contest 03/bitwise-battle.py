
"""
You are given two positive integers X and Y. Your task is to perform the following bitwise operations on them:

AND (&) – Keeps a bit as 1 only if both numbers have 1 in that position.
OR (|) – Keeps a bit as 1 if at least one number has 1 in that position.
XOR (^) – Keeps a bit as 1 only if exactly one number has 1 in that position.

Note: You don't need to convert Decimal number into Binary number, you can directly perform operation on decimal 
number.


Test cases:
1) input :5 3     output: 1 7 6
2) input :10 12     output: 8 14 6
3) input :7 7     output: 7 7 0
4) input :1 15    output: 1 15 14
5) input :8 4    output: 0 12 12
5) input :1023 511   output: 511 1023 512

"""


X, Y = map(int, input().split())

and_bitwise = X & Y
or_bitwise = X | Y
xor_bitwise = X ^ Y

print(and_bitwise, or_bitwise, xor_bitwise)