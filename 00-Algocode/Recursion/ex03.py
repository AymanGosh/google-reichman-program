def sum_from_mid_to_start_end(itr):
    if len(itr) == 1:
        return itr[0]
    mid_elm_index = len(itr) // 2
    return itr[mid_elm_index] + sum_from_mid_to_start_end(
        itr[:mid_elm_index] + itr[mid_elm_index + 1 :]
    )


assert sum_from_mid_to_start_end([1, 2, 3]) == 6
