"""
Given three real numbers a, b, and c as coefficients of a quadratic equation ax^2 + bx + c =0, 
find its roots using the quadratic formula. Print the roots in the appropriate 
format based on their nature: real and distinct, real and equal, or complex.

If the equation has two distinct real roots, print both roots in increasing order, each separated by a space, rounded off to **0 decimal place..
If the equation has two equal real roots, print the root once rounded off to 0 decimal place.
If the equation has complex roots, print Imaginary Roots.

"""

a, b, c = map(int, input().split())
d = b**2 - 4*a*c

if d > 0:
    root1 = (-b - d**0.5) / (2*a)
    root2 = (-b + d**0.5) / (2*a)
    r1 = int(round(root1))
    r2 = int(round(root2))
    if r1 < r2:
        print(r1, r2)
    else:
        print(r2, r1)
elif d == 0:
    root = int(round(-b / (2*a)))
    print(root)
else:
    print("Imaginary Roots")


