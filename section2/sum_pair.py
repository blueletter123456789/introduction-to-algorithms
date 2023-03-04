from bisect import bisect

def sum_pair(ins, x):
    lst = sorted(ins)
    for i, num in enumerate(lst):
        tgt = x - num
        j = max(bisect(lst, tgt) - 1, 0)
        if i != j and (num + lst[j]) == x:
            return True
    
    return False

def sum_pair_another(ins, x):
    lst = sorted(ins)
    i, j = 0, len(lst) - 1
    while i < j:
        if lst[i] + lst[j] == x:
            return True
        if lst[i] + lst[j] < x:
            i += 1
        if lst[i] + lst[j] > x:
            j -= 1
    return False



if __name__ == '__main__':
    import random
    lst = [random.randint(0, 100) for _ in range(7)]
    tgt = lst[2] + lst[5]
    print(lst, tgt)
    print(sum_pair(lst, tgt))
    print(sum_pair_another(lst, tgt))

    lst = [1, 4, 5, 6, 6, 9]
    print(sum_pair(lst, 12))
    print(sum_pair_another(lst, 12))

    print(sum_pair(lst, 8))
    print(sum_pair_another(lst, 8))
