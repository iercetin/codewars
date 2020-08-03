# Consecutive strings
# https://www.codewars.com/kata/56a5d994ac971f1ac500003e

def longest_consec(strarr, k):
    n = len(strarr)
    if n == 0 or k > n or k <= 0:
        return ""
    r = ""
    r_bag = ""
    for x in range(n-k+1):
        r_bag = strarr[x]
        for y in range(x+1,x+k):
            r_bag += strarr[y]            
        if len(r_bag) > len(r):
            r = r_bag
    return r
