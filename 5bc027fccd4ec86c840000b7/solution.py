# Simple sum of pairs
# https://www.codewars.com/kata/5bc027fccd4ec86c840000b7/train/python

def solve(n):
    if n < 10:
        return n
    a = int((len(str(n)) - 1) * '9')
    print("n: {}, a: {}".format(n,a))
    b = n - a
    return sum([int(i) for i in (list(str(a)) + list(str(b)))])