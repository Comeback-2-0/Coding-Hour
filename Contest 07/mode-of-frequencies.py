"""
Aman is studying Biostatistics and has been given a dataset for analysis. She needs to find a special value called the Mode of Frequencies from a list of integers.

Given a list of integers A = [A1, A2, …, AN], follow these steps:

1. Compute the frequency of each distinct number in A.
2. Then, find which frequency value occurs most often among those frequencies.
3. If multiple frequency values occur the same (maximum) number of times, return the smallest such frequency.

In short:

- First, count how often each number appears.
- Then, find which frequency value is most frequent.
- If there’s a tie, pick the smaller frequency.


Test Cases:
Test case 1: 
1
5
1 1 1 1 1

output: 5

Test Case 2:
1
5
1 2 3 4 5

output: 1

Test Case 3:
2
8
1 1 2 2 3 3 4 4
6
1 1 1 2 2 3

output: 2
        1

Test Case 4:
1
9
1 1 2 2 3 3 4 4 5

Output: 
2


"""

t = int(input())

for _ in range(t):
    n = int(input())  
    arr = list(map(int, input().split()))  

    
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1


    freq_count = {}
    for f in freq.values():
        if f in freq_count:
            freq_count[f] += 1
        else:
            freq_count[f] = 1

   
    max_count = max(freq_count.values())

    
    smallest_freq = None
    for f in freq_count:
        if freq_count[f] == max_count:
            if smallest_freq is None or f < smallest_freq:
                smallest_freq = f

    print(smallest_freq)
