def insertion_sort(ins: list[int]) -> list[int]:
    for i in range(1, len(ins)):
        key = ins[i]
        j = i - 1
        while j >= 0 and ins[j] > key:
            ins[j+1] = ins[j]
            j -= 1
        ins[j + 1] = key
    return ins


if __name__ == '__main__':
    A = [5, 2, 4, 6, 1, 3]
    print(insertion_sort(A))
