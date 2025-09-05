"""
At the Codebreaker’s Tournament, participants are challenged with strange puzzles.
One of the puzzles involves two 3-digit secret codes. To unlock the treasure chest, players must apply a special rule:

1. Break down each 3-digit code into its hundreds, tens, and ones digits.
2. Add the digits from the same positions in both numbers.
	(hundreds with hundreds, tens with tens, ones with ones).
3. Multiply all the digit-wise sums together to form the final unlock code.

Your task is to compute this final unlock code.

**Rules:**

- Both inputs will always be 3-digit integers (between 100 and 999).
- The digit-wise sum should be performed position-wise.
- The result is the multiplication of the three sums.

"""

A, B = map(int, input().split())
a1 = A // 100
temp1 = A // 10 
a2 =  temp1 % 10
a3 = A%10

b1 = B // 100
temp2 = B // 10 
b2 =  temp2 % 10
b3 = B%10

result = (a1 + b1) * (a2 + b2) * (a3 + b3)
print(result)
