"""
You are given a positive integer N. Your task is to find two new values by:

Left shifting N by 3 positions (N << 3)

This means shifting all bits of N 3 places to the left, which is the same as multiplying the number by 2³ (8).
Right shifting N by 3 positions (N >> 3)

This means shifting all bits of N 3 places to the right, which is the same as performing integer division by 2³ (8).

Test cases:
1) input : 4    output: 32 0
2) input : 16    output: 128 2 
3) input : 100    output: 800 12
4) input : 7    output: 56 0
5) input : 0     output: 0 0

"""


N = int(input())

left_shift = N << 3   
right_shift = N >> 3  

print(left_shift, right_shift)