def insertion_sort_reverse(ins):
    for i in range(1, len(ins)):
        key = ins[i]
        j = i - 1
        while j >= 0 and ins[j] < key:
            ins[j+1] = ins[j]
            j -= 1
        ins[j+1] = key
    return ins


if __name__ == '__main__':
    lst = [31, 41, 59, 26, 41, 58]
    print(insertion_sort_reverse(lst))
