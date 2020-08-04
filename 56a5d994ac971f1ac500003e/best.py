
def longest_consec(strarr, k):
    n = len(strarr)
    if n == 0 or k > n or k <= 0:
        return ""

    result = ""
    for x in range(n-k+1):
        bag = "".join(strarr[x:x+k])
        if len(bag) > len(result):
            result = bag
    return result