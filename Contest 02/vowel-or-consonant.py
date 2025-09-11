"""
You are given a single lowercase English letter.
If the letter is one of '**a**', '**e**', '**i**', '**o**', '**u**', print "**Vowel**".
Otherwise, print "**Consonant**".

test cases 
1. input : e output: Vowel
2. input : b  output: Consonant 
3. input : o  output: Vowel
4. input : m  output: Consonant 
5. input : u output: Vowel

"""


ch = input()

if ch in "aeiou":
    print("Vowel")
else:
    print("Consonant")