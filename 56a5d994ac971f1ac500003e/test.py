from best import longest_consec
from tests import Test
from os.path import dirname, abspath
import sys
sys.path.append(dirname(dirname(abspath(__file__))))


Test.assert_equals(longest_consec(
    ["zone", "abigail", "theta", "form", "libe", "zas"], 2), "abigailtheta")
Test.assert_equals(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx",
                                   "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1), "oocccffuucccjjjkkkjyyyeehh")
Test.assert_equals(longest_consec([], 3), "")
Test.assert_equals(longest_consec(["itvayloxrp", "wkppqsztdkmvcuwvereiupccauycnjutlv",
                                   "vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2), "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck")
Test.assert_equals(longest_consec(
    ["wlwsasphmxx", "owiaxujylentrklctozmymu", "wpgozvxxiu"], 2), "wlwsasphmxxowiaxujylentrklctozmymu")
Test.assert_equals(longest_consec(
    ["zone", "abigail", "theta", "form", "libe", "zas"], -2), "")
Test.assert_equals(longest_consec(
    ["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 3), "ixoyx3452zzzzzzzzzzzz")
Test.assert_equals(longest_consec(
    ["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 15), "")
Test.assert_equals(longest_consec(
    ["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 0), "")
