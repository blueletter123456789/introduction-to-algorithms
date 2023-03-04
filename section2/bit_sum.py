def bit_sum(ins_a, ins_b):
    n = len(ins_a)
    ins_c = [0] * (n + 1)
    for idx, (a, b) in enumerate(zip(reversed(ins_a), reversed(ins_b))):
        sum_num = a + b + ins_c[n - idx]
        if sum_num <= 1:
            ins_c[n - idx] = sum_num
        elif sum_num == 2:
            ins_c[n - idx] = 0
            ins_c[n - idx - 1] = 1
        else:
            ins_c[n - idx] = 1
            ins_c[n - idx - 1] = 1
    return ins_c


if __name__ == '__main__':
    a = [1, 0, 1]
    b = [0, 1, 1]
    print(bit_sum(a, b))

    a = [1, 1, 0]
    b = [0, 1, 1]
    print(bit_sum(a, b))
