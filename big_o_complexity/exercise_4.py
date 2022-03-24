def count_equalities_in_find(elements_list, value):
    N = len(elements_list)
    op_count = 0
    for i in range(N):
        op_count += 1
        if elements_list[i] == value:
            return op_count
    return op_count

def num_op(elements_list):
    total_op_count = 0
    for el in elements_list:
        total_op_count += count_equalities_in_find(elements_list, el)
    return num_op
