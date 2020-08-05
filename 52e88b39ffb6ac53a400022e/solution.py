# int32 to IPv4
# https://www.codewars.com/kata/52e88b39ffb6ac53a400022e


def int32_to_ip(int32):
    binary_string = "{0:b}".format(int32)

    for x in range(32-len(binary_string)):
        binary_string = "0" + binary_string

    r = []
    for i in range(4):
        r.append(str(int(binary_string[(i*8):(i*8+8)], 2)))
    return ".".join(r)
