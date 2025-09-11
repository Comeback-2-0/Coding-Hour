"""
You are given three integers: **hours**, **minutes**, and **seconds**.
Your task is to calculate the total time in seconds using the rules:

- 1 hour = 3600 seconds
- 1 minute = 60 seconds

The output should be a single integer representing the total seconds.

test cases 
1. input : 2 0 0                   output: 72000
2. input : 0 0 45                  output: 45
3. input : 10 30 0                 output: 37800
4. input : 1000000 0 0             output: 3600000000 
5. input : 0 59 59                 output: 3599

"""


hours, minutes, seconds = map(int, input().split())
total_seconds = hours * 3600 + minutes * 60 + seconds
print(total_seconds)