def binary_search(ins, x):
    l, r = 0, len(ins)
    while l < r:
        m = (l + r) // 2
        if ins[m] == x:
            return m
        elif ins[m] < x:
            l = m
        else:
            r = m
    return -1


def binary_search_recursive(ins, x):
    def _inner(l, r):
        if l >= r:
            return -1
        m = (l + r) // 2
        if ins[m] == x:
            return m
        if ins[m] < x:
            return _inner(m, r)
        else:
            return _inner(l, m)
    return _inner(0, len(ins))


if __name__ == '__main__':
    import random
    lst = sorted([random.randint(0, 100) for _ in range(8)])
    v = random.randint(0, len(lst)-1)
    print(lst[v], lst)

    print(binary_search(lst, lst[v]))
    print(binary_search_recursive(lst, lst[v]))
