"""

A student has just realized that he has a mountain of homework to finish before tomorrow!
He has several worksheets to complete, and each worksheet contains exactly Y questions.
Chef has already solved X questions, but he can only manage to complete at most 10 worksheets before the deadline.

To get a full score, Chef needs to solve at least 100 questions in total.
Your task is to determine whether Chef can still achieve a full score with the time he has left.

Test cases:
Test Case 0: input: 73 4 output: Yes
Test Case 1: input: 0 10   output: Yes
Test Case 2: input: 47 5  output: No
Test Case 3: input: 95 1   output: Yes
Test Case 4: input: 80 1 output: No
Test Case 5: input: 0 0  output: No

"""
X, Y = map(int, input().split())

if X + (10 * Y) >= 100:
    print("Yes")
else:
    print("No")
