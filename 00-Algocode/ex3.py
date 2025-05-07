
def heap_find(A, z):
    stack = [0]
    while stack:
        i = stack.pop()
        if i >= len(A):
            continue
        if A[i] > z:
            continue
        if A[i] == z:
            return i
        stack.append(2 * i + 2)  # Go R
        stack.append(2 * i + 1)  # Go L
    return None
