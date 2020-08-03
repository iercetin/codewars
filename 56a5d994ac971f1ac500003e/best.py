"""
def longest_consec(strarr, k):
    result = ""
    
    if k > 0 and len(strarr) >= k:
        for index in range(len(strarr) - k + 1):
            s = ''.join(strarr[index:index+k])
            if len(s) > len(result):
                result = s
            
    return result
"""

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