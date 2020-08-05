# Crack the PIN
# https://www.codewars.com/kata/5efae11e2d12df00331f91a6

import hashlib


def clear_string(n):
    l = len(str(n))
    r = ""
    for i in range(5-l):
        r += "0"
    return r + str(n)


hashes = {}

# 10 ** 5
for i in range(10**5):
    pin = clear_string(i)
    hash = hashlib.md5(bytes(pin, encoding="utf-8")).hexdigest()
    hashes[hash] = pin


def crack(hash):
    return hashes[hash]
