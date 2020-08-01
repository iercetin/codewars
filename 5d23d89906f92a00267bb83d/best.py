# New Cashier Does Not Know About Space or Shift
# https://www.codewars.com/kata/5d23d89906f92a00267bb83d/solutions/python

MENU = ["Burger", "Fries", "Chicken", "Pizza", "Sandwich", "Onionrings", "Milkshake", "Coke"]

def get_order(order):
    return " ".join([name for name in MENU for i in range(order.count(name.lower()))])