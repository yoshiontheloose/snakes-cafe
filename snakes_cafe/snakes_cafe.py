from typing import Counter

order_list = []

def menu():
  menutxt = """
  **************************************
  **    Welcome to the Snakes Cafe!   **
  **    Please see our menu below.    **
  **
  ** To quit at any time, type "quit" **
  **************************************

  Appetizers
  ----------
  Wings
  Cookies
  Spring Rolls

  Entrees
  -------
  Salmon
  Steak
  Meat Tornado
  A Literal Garden

  Desserts
  --------
  Ice Cream
  Cake
  Pie

  Drinks
  ------
  Coffee
  Tea
  Unicorn Tears

  ***********************************
  ** What would you like to order? **
  ***********************************
  """
  print(menutxt)
  
  user_order = ''
  while user_order != "quit":
    user_order = input("> ")
    order_list.append(user_order)
    item_count = order_list.count(user_order)
    if user_order == "quit":
      break
    print(f"{item_count} order of {user_order} have been added to your meal")



# add order to order_list to show user their order
# order needs to be counted, replace x/turn into a variable
# count needs to be displayed in the confirmation
# count/loop input until user types quit


# tells terminal to run menu function
if __name__ == "__main__":
  menu()

  