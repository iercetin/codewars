# A disguised sequence (I)
# https://www.codewars.com/kata/563f0c54a22b9345bf000053/train/python


def fcn(n):
    vals = [1, 2]

    while len(vals) <= n:
        n0 = vals[len(vals)-2]
        n1 = vals[len(vals)-1]
        n2 = -6*(n0*n1) / ((-5*n0)+n1)

        try:
            int(n2)
            vals.append(n2)
        except Exception as e:
            break

    print(vals)

    return int(vals[len(vals)-1])


print(fcn(21123123123123))
