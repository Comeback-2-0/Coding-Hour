"""
You are given two integers: **total_bill** and **number_of_people**.
Your task is to calculate how much each person pays if the bill is split equally.

The result should be an **integer value** since everyone pays a whole number.

"""

""" 
test cases 
1. input : 250 2  output: 125 
2. input : 500 10  output: 50 
3. input : 123456789 9  output: 13717421 
4. input : 1 1  output: 1 
5. input : 1000000000 1000000 output: 1000  

"""
total_bill, number_of_people = map(int, input().split())
print(total_bill // number_of_people)
