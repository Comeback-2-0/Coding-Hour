"""

In a digital puzzle, each number hides a secret — the number of 1s in its binary representation. 
You need to count how many 1 bits are there in the binary form of a given integer.

Test cases:
Test Case 0: input: 13  output: 3
Test Case 1: input: 0   output: 0
Test Case 2: input: 255  output: 8
Test Case 3: input: 1023   output: 10



"""

n=int(input())
c=0
while(n!=0):
    a=n&1
    n=n>>1
    if(a==1):
        c=c+1
print(c)