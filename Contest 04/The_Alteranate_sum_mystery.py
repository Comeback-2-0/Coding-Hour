"""

A mathematician challenges you to find the alternating sum of the first N natural numbers. 
That means: 1 - 2 + 3 - 4 + 5 - 6 … up to N. Your task is to compute this sum using loops.

Test cases:
Test Case 0: input:5   output: 3
Test Case 1: input:1   output: 1
Test Case 2: input:6  output: -3   
Test Case 3: input:10  output: -5
Test Case 4: input: 1000000  output: -500000


"""

n=int(input())
s=0
i=1
while(i<=n):
    if(i%2==0):
        s=s-i
    else:
        s=s+i
    i=i+1
    
print(s)