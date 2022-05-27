"""Autor: Elizeu Ferreira
   CSE: 110
   09 Prove: Assignment Milestone
"""
#Shopping Cart Program
print("Welcome to the Shopping Cart Program!")
print()
print("Please select one of the following:")
print("1. Add item\n2. View cart\n3. Remove item\n4. Compute total\n5. Quit")

cart = []

action = 0
while action != '5':

  action = input('Please enter an action: ')

  if action == '1':
    name = input('What item would you like to add? ')
    price = input('What is the price?: ')

    item = {'name':name, 'price': price}
    cart.append(item)
    print(item['name'], 'has been added to the cart.')
  elif action == '2':
    print('The contents of the shopping cart are:')
    for item in cart:
      print(f"{cart.index(item) + 1}. {item['name']} - ${item['price']}")
  elif action == '3':
    for item in cart:
      print(f"{cart.index(item) + 1}. {item['name']}")
    remove = int(input('Which item would you like to remove?: '))
    if remove > len(cart):
      print("Sorry, that is not a valid item number.")
    cart.pop(remove - 1)
    print("Item removed")
  elif action == '4':
    soma = 0
    for item in cart:
      soma += float(item['price'])
    print(f'The total price of the items in the shopping cart is: ${soma:.2f}')
  elif action == '5':
    print('Thank you. Goodbye.')

