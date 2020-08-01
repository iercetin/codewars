from solution import get_order
from os.path import dirname, abspath
import sys
sys.path.append(dirname(dirname(abspath(__file__))))
from tests import Test


Test.assert_equals(get_order("milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"),
                            "Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke");
Test.assert_equals(get_order("pizzachickenfriesburgercokemilkshakefriessandwich"),
                    "Burger Fries Fries Chicken Pizza Sandwich Milkshake Coke")
Test.assert_equals(get_order("burgerfriesfriesfriesfriesfriespizzasandwichcokefriesburger"),
                    "Burger Burger Fries Fries Fries Fries Fries Fries Pizza Sandwich Coke")