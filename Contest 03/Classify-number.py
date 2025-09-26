"""

You are given an integer n. If it is divisible by both 3 and 5, 
print "Divisible by 3 and 5". If it is divisible only by 3, print "Divisible by 3". 
If it is divisible only by 5, print "Divisible by 5". Otherwise, print "Not Divisible".

Test cases:
1) input : 15     output: Divisible by 3 and 5
2) input : 5      output: Divisible by 5
3) input : 7      output: Not Divisible
4) input : 9      output: Divisible by 3 
5) input : -30    output: Divisible by 3 and 5


"""

n = int(input())

if n % 3 == 0 and n % 5 == 0:
    print("Divisible by 3 and 5")
elif n % 3 == 0:
    print("Divisible by 3")
elif n % 5 == 0:
    print("Divisible by 5")
else:
    print("Not Divisible")