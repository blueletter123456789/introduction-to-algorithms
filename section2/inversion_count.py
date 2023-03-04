def merge(ins: list, p: int, q: int, r: int) -> int:
    lst_l = ins[p:q]
    lst_r = ins[q:r]

    cnt = i = j = 0
    k = p
    while i < len(lst_l) and j < len(lst_r):
        if lst_l[i] <= lst_r[j]:
            ins[k] = lst_l[i]
            i += 1
        else:
            ins[k] = lst_r[j]
            j += 1
            cnt += len(lst_l) - i
        k += 1
        
    while i < len(lst_l):
        ins[k] = lst_l[i]
        k += 1
        i += 1
    while j < len(lst_r):
        ins[k] = lst_r[j]
        k += 1
        j += 1

    return cnt



def inversion_count(ins, le, ri):
    if ri - le > 1:
        m = (le + ri) // 2
        return (inversion_count(ins, le, m) +
                inversion_count(ins, m, ri) +
                merge(ins, le, m, ri))
    return 0


if __name__ == '__main__':
    lst = [2, 3, 8, 6, 1]
    l, r = 0, len(lst)
    print(inversion_count(lst, l, r))

    lst = [6, 5, 4, 3, 2, 1]
    l, r = 0, len(lst)
    print(inversion_count(lst, l, r))
