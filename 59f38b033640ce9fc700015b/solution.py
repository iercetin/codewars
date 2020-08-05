# Sum of prime-indexed elements
# https://www.codewars.com/kata/59f38b033640ce9fc700015b/train/python

import math


def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


def total(arr):
    l = len(arr)
    result = 0
    for i in range(2, l):
        if is_prime(i):
            #print("Num: {}, IsP: {}, To: {}".format(i,is_prime(i),arr[i]))
            result += arr[i]

    return result
