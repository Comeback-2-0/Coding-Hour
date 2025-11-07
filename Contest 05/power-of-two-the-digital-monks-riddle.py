"""
In an ancient monastery, there lived a digital monk who believed that numbers possessing the “Power of Two” had special harmony.
He challenges you to identify whether a given integer N possesses this divine power.

A number is said to be a power of two if it can be expressed as 2^x where x is an integer (like 1, 2, 4, 8, 16, …).
Your task is to determine whether the given number has this property or not.

Test cases:
Test Case 0: input: 16 output: YES
Test Case 1: input: 1   output: YES
Test Case 2: input: 3  output: N0
Test Case 3: input: 0  output: NO
Test Case 4: input: -8 output: NO
Test Case 5: input: 1024  output: YES

"""

N = int(input())
if N > 0 and (N & (N - 1)) == 0:
    print("YES")
else:
    print("NO")
