from best import bracket_pairs
from tests import Test
from os.path import dirname, abspath
import sys
sys.path.append(dirname(dirname(abspath(__file__))))


Test.assert_equals(bracket_pairs("len(list)"), {
                   3: 8}, "Single pair of brackets")
Test.assert_equals(bracket_pairs("string"), {}, "String without brackets")
Test.assert_equals(bracket_pairs(""), {}, "Empty string")
Test.assert_equals(bracket_pairs("def f(x"), False, "unmatched bracket")
Test.assert_equals(bracket_pairs(")("), False, "invalid brackets")
Test.assert_equals(bracket_pairs("(a(b)c()d)"), {
                   0: 9, 2: 4, 6: 7}, "nested brackets")
Test.assert_equals(bracket_pairs("f(x[0])"), {1: 6}, "ignore square brackets")
