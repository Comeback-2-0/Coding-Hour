"""
Given a number 𝑛, calculate the sum of the first 𝑛 natural numbers using a loop.
"""

# Approach 1: Using For loop
n = int(input())
total = 0
for i in range(1, n + 1):
    total += i
print(total)


# Approach 2: Using While loop
"""
n = int(input())
total = 0
i = 1
while i <= n:
    total += i
    i += 1
print(total)
"""

#Approach 3:
"""
n = int(input())
sum = (n*(n+1))//2
print(sum)

"""