# New Cashier Does Not Know About Space or Shift
# https://www.codewars.com/kata/5d23d89906f92a00267bb83d/solutions/python

items = ["Burger", "Fries", "Chicken", "Pizza",
         "Sandwich", "Onionrings", "Milkshake", "Coke"]


def get_order(order):
    r = ""
    result = []
    clean = order
    for x in range(len(order)):
        for y in range(len(order)+1):
            substr = order[x:y]
            if substr.capitalize() in items:
                r += substr.capitalize() + " "
                result.append(substr.capitalize())
                #print("Found: {}, x: {}, y: {}".format(substr,x,y))

    amounts = {}
    for result_item in result:
        if result_item in amounts:
            amounts[result_item] = amounts[result_item] + 1
        else:
            amounts[result_item] = 1

    l = []
    for item in items:
        if item in amounts:
            for i in range(amounts[item]):
                l.append(item)

    return " ".join(l)
