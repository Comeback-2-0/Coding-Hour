"""

Two friends, Riya and Karan, love collecting numbers.

- Riya has a list of integers called A.
- Karan has a list of integers called B.

They decide to find the numbers that are unique to each of them —
that is, the numbers that appear in either list but not in both.

This operation is called the symmetric difference of two lists.

Your task is to help them find all such unique numbers and print them in ascending order.

Test Cases:
0: input  
4
1 2 3 4
4
3 4 5 6

output: 1 2 5 6

1: input 
4
2 4 6 8
3
3 5 7

output: 2 3 4 5 6 7 8

2: input
5
1 2 3 4 5
4
2 4 6 8

output: 1 3 5 6 8

3: input
0

3
1 2 3

output:1 2 3

4:input
5
-2 -1 0 1 2
4
-1 0 1 3

output:-2 2 3

"""

n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

setA = set(A)
setB = set(B)

result = sorted((setA - setB) | (setB - setA))

print(result)