"""

Arjun has a special collection of odd numbers.
He took the first N odd numbers — for example:
if N = 5, the numbers are 1, 3, 5, 7, 9.

Then, Arjun created a new list from them with N + K - 1 elements.
He did this by copying one of the numbers exactly K times,
while keeping all the others only once.

He then calculated the sum (S) of all the numbers in this new list.
Unfortunately, he forgot which number he had repeated!

Your task is to help Arjun find out which odd number was repeated K times.

It is guaranteed that for the given input values, a valid answer always exists.


Test Cases:
1: input: 
2
1 2 3
2 2 7

output: 
2
3

2:input:
1
2 3 10

output:
3

3: input:
3
2 3 10
3 4 21
4 5 40

output:
3
4
6

4:input:
1
10 6 200

output:20


"""
T = int(input())
for _ in range(T):
    N, K, S = map(int, input().split())
    total_sum = N * N
    repeated_num = (S - total_sum) // (K - 1)
    print(repeated_num)