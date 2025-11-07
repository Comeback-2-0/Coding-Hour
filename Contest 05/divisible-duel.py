"""

Alice loves working with numbers. One day, she takes two integers X and Y (Y ≥ X) and becomes curious about the numbers between them.

She looks at all integers between X and Y (inclusive) that are divisible by X.
Among these numbers, she separates them into even and odd numbers.

Let the sum of all even numbers be Seven, and the sum of all odd numbers be Sodd.

If Seven ≥ Sodd, Alice will be happy; otherwise, she will be sad.
Your task is to determine whether Alice will be happy or not for each test case.

Test cases:
Test Case 0: 
input:  3        output: YES
        1 4              NO
        3 9              YES
        4 100

Test Case 1: 
input: 1      output:  YES
       5 20  

Test Case 2: 
input: 2        output: YES
       8 17             YES
       10 10  
Test Case 3: 
input: 3        output: YES
       2 6              NO
       7 49             YES
       6 12   
Test Case 4: 
input: 1        output: NO
       9 27 


"""

T = int(input())
for _ in range(T):
    X, Y = map(int, input().split())
    Seven = 0
    Sodd = 0
    for num in range(X, Y + 1):
        if num % X == 0:
            if num % 2 == 0:
                Seven += num
            else:
                Sodd += num
    if Seven >= Sodd:
        print("YES")
    else:
        print("NO")
