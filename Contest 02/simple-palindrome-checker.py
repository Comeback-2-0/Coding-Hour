"""
A palindrome is a number that reads the same forwards and backwards (e.g., 121).
You are given a three-digit integer. Your task is to check if the number is a palindrome.

⚠️ **Important Rule**:

You are **not allowed** to use string functions.
Use only mathematical operators (/ and %).

test cases 
1. input : 454 output: Palindrome
2. input : 989 output: Palindrome
3. input : 101  output: Palindrome
4. input : 222 output: Palindrome 
5. input : 345 output: Not a Palindrome

"""
n = int(input())

first = n // 100
last = n % 10

if first == last:
    print("Palindrome")
else:
    print("Not a Palindrome")