def sum_from_last_elm(itr):
    if len(itr) == 0:
        return 0
    return itr[len(itr) - 1] + sum_from_last_elm(itr[:-1])


assert sum_from_last_elm([1, 2, 3]) == 6
