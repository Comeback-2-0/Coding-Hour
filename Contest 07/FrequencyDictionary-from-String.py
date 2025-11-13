
"""

You are given a string S consisting of lowercase and uppercase English letters. Your task is to create a dictionary that
stores each unique character in the string as a key and its frequency (count) as the corresponding value.

The dictionary must maintain the order of first appearance of each character in the string.

"""


s=input()
dict={}
for i in s:
    if i in dict:
        dict[i]=dict[i]+1
    else:
        dict[i]=1
print(dict)