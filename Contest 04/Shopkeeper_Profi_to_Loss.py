"""

A shopkeeper wants to quickly find out whether he made a profit, loss, or neither after selling a product. You are given the Cost Price (CP) and Selling Price (SP) of the product.

Your task is to calculate:

Whether there is a Profit, Loss, or No Profit No Loss.
and the amount of profit or loss.



Test Cases:
Test Case 0: input: 100 150  output: Profit 50
Test Case 1: input: 200 170   output: Loss 30
Test Case 2: input: 120 120  output: No Profit, No Loss 0



"""




cost_price, selling_price = map(int, input().split())

if selling_price > cost_price:
    outcome = "Profit"
    amount = selling_price - cost_price
elif selling_price < cost_price:
    outcome = "Loss"
    amount = cost_price - selling_price
else:
    outcome = "No Profit, No Loss"
    amount = 0

print(f"{outcome} {amount}")