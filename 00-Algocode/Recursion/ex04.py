def avg(itr):
    if len(itr) == 1:
        return itr[0]
    return (avg(itr[:-1]) * (len(itr) - 1) + itr[-1]) / len(itr)


assert avg([1, 2, 3]) == 2
