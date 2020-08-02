from os.path import dirname, abspath
import sys
sys.path.append(dirname(dirname(abspath(__file__))))
from tests import Test
from solution import solve


Test.assert_equals(solve(18),18)
Test.assert_equals(solve(29),11)
Test.assert_equals(solve(45),18)
Test.assert_equals(solve(1140),33)
Test.assert_equals(solve(7019),35)