# Snail
# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1


def first_and_right(snail_map):
    axis = len(snail_map)

    if len(snail_map) < 1:
        return []

    r = snail_map[0]
    remainings = []

    for i in range(1, axis):
        row = snail_map[i][-1:][0]
        r_row = snail_map[i][0:-1]

        r.append(row)
        remainings.append(r_row)

    return [r, remainings]


def last_and_left(snail_map):
    axis = len(snail_map)

    if len(snail_map) < 1:
        return []

    b = snail_map[axis-1]
    b.reverse()
    r = b

    remainings = []

    done_row = []
    for i in range(axis-1):
        row = snail_map[i][0]
        r_row = snail_map[i][1:]

        done_row.append(row)

        # r.append(row)
        remainings.append(r_row)

    done_row.reverse()
    r = r + done_row

    return [r, remainings]


def snail(snail_map):
    if len(snail_map) < 1:
        return []

    axis = len(snail_map)

    winner = []

    remainings = snail_map
    count = 0
    for i in range(axis):
        if count % 2 == 0:
            c = first_and_right(remainings)
        else:
            c = last_and_left(remainings)

        remainings = c[1]
        returns = c[0]

        for returned in returns:
            winner.append(returned)

        count += 1

    return winner
