# Custom Christmas Tree
# https://www.codewars.com/kata/5a405ba4e1ce0e1d7800012e

def custom_christmas_tree(chars, n):
    r = ""
    c = 0
    for i in range(1,n+1):
        rem = n - i
        l = " "*rem
        for x in range(i):
            if x is not 0:
                l += " "
            l += chars[c%len(chars)]
            c += 1
        l += "\n"
        r += l

    bl = int(len(l)/2)-1
    bottom = ""
    for j in range(int(n/3)):
        bottom += " " * bl + "|"
        if j is not int(n/3)- 1:
            bottom += "\n"
    r += bottom
    return r