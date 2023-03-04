import random


def selection_sort(ins):
    n = len(ins)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if ins[min_idx] > ins[j]:
                min_idx = j
        ins[i], ins[min_idx] = ins[min_idx], ins[i]
    return ins


if __name__ == '__main__':
    lst = [random.randint(0, 100) for _ in range(5)]
    print(lst)
    print(selection_sort(lst))
