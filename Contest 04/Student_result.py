"""
Write a Python program to read the marks of a student in three subjects and determine the final result based on the following conditions:

The student will be declared “Passed” if he/she secures more than 50 marks in all three subjects.
The student will be declared “Passed by Grace” if:
He/she secures more than 50 marks in any two subjects,
More than 40 marks in the third subject, and
The average marks of all three subjects is greater than 50.
In all other cases, the student will be declared “Failed”.

Test cases:
Test Case 0: input: 55 60 45  output: Result: Passed by Grace
Test Case 1: input: 65 70 80   output: Result: Passed
Test Case 2: input: 40 45 55  output: Result: Failed
Test Case 3: input: 52 58 42  output: Result: Passed by Grace
Test Case 4: input: 30 55 60  output: Result: Failed

"""

m1, m2, m3 = map(int, input().split())
avg = (m1 + m2 + m3) / 3

if m1 > 50 and m2 > 50 and m3 > 50:
    print("Result: Passed")
elif ((m1 > 50 and m2 > 50 and m3 > 40) or
      (m1 > 50 and m3 > 50 and m2 > 40) or
      (m2 > 50 and m3 > 50 and m1 > 40)) and avg > 50:
    print("Result: Passed by Grace")
else:
    print("Result: Failed")