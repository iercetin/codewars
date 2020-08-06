from os.path import dirname, abspath
import sys
sys.path.append(dirname(dirname(abspath(__file__))))

from solution import custom_christmas_tree
from tests import Test


Test.assert_equals(custom_christmas_tree("*@o",3),
"""  *
 @ o
* @ o
  |""")
  
Test.assert_equals(custom_christmas_tree("*@o",6),
"""     *
    @ o
   * @ o
  * @ o *
 @ o * @ o
* @ o * @ o
     |
     |""")

Test.assert_equals(custom_christmas_tree("1234",6),
"""     1
    2 3
   4 1 2
  3 4 1 2
 3 4 1 2 3
4 1 2 3 4 1
     |
     |""")

Test.assert_equals(custom_christmas_tree("123456789",3),
"""  1
 2 3
4 5 6
  |""")
