def linear_search(ins, v):
    for idx, num in enumerate(ins):
        if v == num:
            return idx

    return None


if __name__ == '__main__':
    lst = [31, 41, 59, 26, 41, 58]
    print(linear_search(lst, 26))
    print(linear_search(lst, 99))
