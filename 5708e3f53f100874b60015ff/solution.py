# Pairing brackets
# https://www.codewars.com/kata/5708e3f53f100874b60015ff


def bracket_pairs(string):
    result = {}

    if string == "":
        return {}

    allow = 0
    no_brackets = True
    for i in range(len(string)-1):
        el = string[i]

        if allow < 1 and el == ")":
            return False

        if el == "(":
            no_brackets = False
            allow += 1
            skip = 0
            substring = string[i+1:]

            for idx in range(len(substring)):
                els = substring[idx]

                if skip == 0 and els == ")":
                    #print("Found {}:{}".format(i,idx+i+1))
                    result[i] = idx+i+1
                    break

                if els == "(":
                    skip += 1
                if els == ")":
                    skip -= 1

        if el == ")":
            allow -= 1

    if no_brackets:
        return {}

    if len(result) == 0:
        result = False

    return result


print(bracket_pairs(")())x))))x))x)))x)))())()))(("), False)
print(bracket_pairs("((x))()"), {1: 3, 0: 4, 5: 6})
print(bracket_pairs("()(x)"), {0: 1, 2: 4})
print(bracket_pairs("()())())())))()()x)))x)x)x))"), False)
