from typing import Counter


def opening():
  menu = """
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
  print(menu)


if __name__ == "__main__":
  opening()

  Order typed into terminal(any words)
  Count
  empty list for orders

  while loop not equal to quit
  add logic for orders added with their counts

  order needs to go into new list
  count needs to be changed 