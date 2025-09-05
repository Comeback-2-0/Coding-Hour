""" 
You are given three integers representing the **length(l)**, **breadth(b)**, and **height(h)** of a cuboid.
The **perimeter of a cuboid** is the sum of all its edge lengths.
It can be calculated using the formula:

**Perimeter = 4 × (l + b + h)**

Your task is to compute and print the perimeter of the cuboid.
"""

l, b, h = map(int, input().split())
print(4 * (l + b + h))
