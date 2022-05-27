"""
Assignments: 03 Prove/Milestone
Subjet: Meal Price Calculator
Autor: Elizeu Ferreira
"""

# Enter a price number for child´s meal, example. 5.50 (floating point numbers)
price_child = float(input("What is the price of a child`s meal? "))

# Enter a price number for adult´s meal, example. 10.00 (floating point numbers)
price_adult = float(input("What is the price of an adult´s meal? "))

# Enter a whole number, example 4
children = int(input("How many children are there "))

# Enter a whole number, example 3
adult = int(input("How many adults are there? "))

# Enter a whole number for sales tax
sales_tax = float(input("What`s the sales tax rate? "))

child = price_child * children
adult = price_adult * adult 
total = float(sales_tax) * (child + adult) /100
ca = child + adult

print()# display a blank line
print("..................")
print(f"subtotal: ${ca:.2f}")
print(f"Sales tax: ${total}")
print("Total: $", child + adult + total)
print("..................")

change_num = child + adult + total
print()# display a blank line
amount = int(input("What is the payment amount? "))
amount_num = amount - change_num
print(f"Change: ${amount_num:.2f}")













