def sum_from_start_end_to_mid(itr):
    if len(itr) < 2:
        return itr[0]
    sum = itr[0] + itr[len(itr) - 1] + sum_from_start_end_to_mid(itr[1 : len(itr) - 1])
    return sum


assert sum_from_start_end_to_mid([1, 2, 3]) == 6
