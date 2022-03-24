def min(number_list):
    min_val = number_list[0]
    for el in number_list:
        if el < min_val:
            min_val = el
    return min_val

def get_product(number_list, i, j):
    return number_list[i] * number_list[j]

def get_row_product(number_list, i):
    N = len(number_list)
    total = 0
    for j in range(N):
        total += get_product(number_list, i, j)
    return total

def check_min_divides_product(number_list):
    N = len(number_list)
    min_el = min(number_list)
    total = 0
    for i in range(N):
        total += get_row_product(number_list, i)
    if total % min_el == 0:
        return True
    return False

print(check_min_divides_product([4, 6, 8, 2]))
