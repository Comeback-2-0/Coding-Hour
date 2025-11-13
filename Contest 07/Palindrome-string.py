"""

Riya loves palindromic strings, but this time she wants something more interesting.

You are given two strings, A and B, consisting only of lowercase English letters. Your task is to determine whether it is possible to choose non-empty substrings s1 (from string A) and s2 (from string B) such that their concatenation (s1 + s2) forms a palindrome of length ≥ 3.

Here, '+' represents string concatenation.

You need to print "Yes" if such a palindrome can be formed, otherwise "No".


Test cases:
Test case : 1) 
2
a
aa
cvt
dfg

output:
Yes
No

Test case : 2) 
1
xyz
zyui

output: Yes

Test case: 3) 
2
a
a
abc
def

output: 
No
No

Test case: 4) 
1
top
pot

output: Yes
"""

t = int(input())
for _ in range(t):
    a = input()
    b = input()
    c = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)+1):
            for k in range(len(b)):
                for l in range(k+1, len(b)+1):
                    x = a[i:j] + b[k:l]
                    if len(x) >= 3 and x == x[::-1]:
                        c = c + 1
    if c >= 1:
        print('Yes')
    else:
        print('No')


