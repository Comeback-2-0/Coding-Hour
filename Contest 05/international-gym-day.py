"""
To celebrate International Gym Day, the Steveland Gym is offering an exciting deal on its lifetime membership.

Steve loves working out and decides to take a few trial sessions before committing.
Each trial session costs 1 coin, but there’s a catch — every trial session gives Steve an additional D% discount on the lifetime membership cost!

Given the original membership cost (X coins) and Steve’s total budget (Y coins), your task is to determine:

- The minimum number of trial sessions Steve must attend so that he can afford the membership.

If Steve cannot buy the membership no matter how many sessions he takes, print -1.


**Rules:**
1. Each trial session reduces Steve’s coins by 1 (session fee).
2. Each trial session gives an extra D% discount on X.
3. After attending n sessions, Chef’s:<br/>
- Remaining coins = Y - n
- Discounted price = X * (100 - n*D) / 100
4. Steve can buy the membership when Y - n >= discounted price and n ≥ 0.

Test cases:
Test Case 0: 
input:        output: 0
3                     2
2 2 2                 -1
5 40 38
3 26 15  

Test Case 1: 
input:         output: 0
2                      -1    
1 10 10
5 20 18  

Test Case 2: 
input:       output: 10
1
4 30 28  

Test Case 3: 
input:      output: -1
2                    4
2 40 20
5 50 45  

Test Case 4: 
input:      output: -1
2                   -1
2 10 9
5 20 19 

"""

T = int(input())
for _ in range(T):
    D, X, Y = map(int, input().split())
    ans = -1
    for n in range(0, 101): 
        discounted_price = X * (100 - n * D) / 100
        remaining_coins = Y - n
        if remaining_coins >= discounted_price and remaining_coins >= 0:
            ans = n
            break
    
    print(ans)