def merge(org_lst, p, q, r):
    # 分割
    lst_l = org_lst[p:q]
    lst_r = org_lst[q:r]

    # 番兵を設定
    lst_l.append(float('inf'))
    lst_r.append(float('inf'))

    i = j = 0
    for k in range(p, r):
        if lst_l[i] <= lst_r[j]:
            org_lst[k] = lst_l[i]
            i += 1
        else:
            org_lst[k] = lst_r[j]
            j += 1

    return org_lst


def merge_sort(ins, le, ri):
    # 擬似コードの条件にする場合はmiの値に+1
    if ri - le <= 1:
        return
    mi = (le + ri) // 2
    merge_sort(ins, le, mi)
    merge_sort(ins, mi, ri)
    merge(ins, le, mi, ri)


if __name__ == '__main__':
    import random
    lst = [random.randint(0, 100) for _ in range(8)]
    l, r = 0, len(lst)
    merge_sort(lst, l, r)
    print(lst)
