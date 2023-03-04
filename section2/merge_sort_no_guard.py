def merge(ins, p, q, r):
    lst_l = ins[p:q]
    lst_r = ins[q:r]
    i = j = 0
    k = p
    while i < (q - p) and j < (r - q):
        if lst_l[i] <= lst_r[j]:
            ins[k] = lst_l[i]
            i += 1
        else:
            ins[k] = lst_r[j]
            j += 1
        k += 1
    
    while i < (q - p):
        ins[k] = lst_l[i]
        i += 1
        k += 1

    while j < (r - q):
        ins[k] = lst_r[j]
        j += 1
        k += 1



def merge_sort(ins, le, ri):
    if ri - le <= 1:
        return
    mi = (le + ri) // 2
    merge_sort(ins, le, mi)
    merge_sort(ins, mi, ri)
    merge(ins, le, mi, ri)
    return ins


if __name__ == '__main__':
    import random

    lst = [random.randint(0, 100) for _ in range(8)]
    l, r = 0,  len(lst)
    print(lst)
    print(merge_sort(lst, l, r))
