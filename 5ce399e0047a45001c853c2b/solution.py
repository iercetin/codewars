# Sums of Parts
# https://www.codewars.com/kata/5ce399e0047a45001c853c2b

def parts_sums(ls):
    ls.reverse()
    t = 0
    r = [t]
    for i in ls:
        t += i
        r.append(t)
    r.reverse()
    return r
        
