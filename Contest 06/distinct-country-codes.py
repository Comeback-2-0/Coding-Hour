"""
You are given a string S consisting of uppercase English letters.
A country code is any two-letter combination of consecutive characters in the string.

Your task is to determine how many distinct country codes appear in S.

Example
For example:
If S = "INBY",
the 2-letter substrings are:
"IN", "NB", and "BY".
There are 3 distinct country codes → output 3.

1: input: 
1
HELLO

output: 4

2: input:
3
ABC
AABB
ZZXX

output:
2
3
3

3: input: 
1
AAAA

output: 1

4: input:
1
ABCDEFGHIJKLMNOP

output:15


"""

t = int(input())

for _ in range(t):
    s = input()
    codes = set()   

    for i in range(len(s) - 1):
        code = s[i] + s[i+1]
        codes.add(code)

    print(len(codes))