# New Cashier Does Not Know About Space or Shift
# https://www.codewars.com/kata/5d23d89906f92a00267bb83d/solutions/python

MENU = ["Burger","Fries","Chicken","Pizza","Sandwich","Onionrings","Milkshake","Coke"]

def get_order(order):
    result = []
    for item in MENU:
        result.extend([item for _ in range(order.count(item.lower()))])
    return " ".join(result)




import sys
sys.path.append('C:\\Users\\ibocan\\Desktop\\Python\\codewars')
from tests import Test

Test.assert_equals(get_order("milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"),
                            "Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke");
Test.assert_equals(get_order("pizzachickenfriesburgercokemilkshakefriessandwich"),
                    "Burger Fries Fries Chicken Pizza Sandwich Milkshake Coke")
Test.assert_equals(get_order("burgerfriesfriesfriesfriesfriespizzasandwichcokefriesburger"),
                    "Burger Burger Fries Fries Fries Fries Fries Fries Pizza Sandwich Coke")