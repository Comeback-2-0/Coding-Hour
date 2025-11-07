"""
You are asked to calculate the total number of working hours in a given year.

In this company, employees work Monday to Friday, and each working day has 8 working hours.
The year always starts on a Monday.

You are given:

- The year (integer)
- The number of public holidays (that fall on working days)

Your task is to find and print the total working hours in that year.

Test cases:
Test Case 0: input: 2023 10 output: 2008
Test Case 1: input: 2024 8  output: 2032
Test Case 2: input: 1900 0  output: 2088
Test Case 3: input: 2000 15  output: 1976
Test Case 4: input: 2021 12 output: 1992


"""

year, holidays = map(int, input().split())
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    total_days = 366
else:
    total_days = 365
weekend_days = 104 
working_days = total_days - weekend_days - holidays
working_hours = working_days * 8
print(working_hours)
