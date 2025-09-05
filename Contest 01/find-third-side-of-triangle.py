"""
Given the perimeter of a triangle and the lengths of two sides, write a program to find the length of the third side. If the third side is not positive or does not form a valid triangle, print -1.

Note:-
A valid triangle must satisfy the triangle inequality for all sides:
a+b>c, 
b+c>a, 
c+a>b 
where c is the length of the third side.
"""
P, a, b = map(int, input().split())
c = P - (a + b)
if c > 0 and a + b > c and b + c >a and c+a>b:
    print(c)
else:
    print(-1)
