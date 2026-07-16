def count_comparisons_in_find(elements_list, value):
    """
    Counts the number of comparisons required to find a value in a list.
    """
    N = len(elements_list)
    comparison_count = 0
    for i in range(N):
        comparison_count += 1
        if elements_list[i] == value:
            return comparison_count
    return comparison_count

def num_comparisons(elements_list):
    """
    For the given input, counts the total number of comparisons that
    are required to find each value in a list inside that same list.
    """
    total_comparison_count = 0
    # Iterate over each value in the list
    for el in elements_list:
        # Search for the current value in the list and count the number of comparisons required
        total_comparison_count += count_comparisons_in_find(elements_list, el)
    return total_comparison_count

### Uncomment this to check your guess
# N = 100
# size_multiplier = 10
# best_case_solution = lambda N: [1 for _ in range(N)]
# worst_case_solution = lambda N: range(N)
# best_case_complexity_multiplyer = num_comparisons(best_case_solution(size_multiplier*N)) / num_comparisons(best_case_solution(N))
# worst_case_complexity_multiplyer = num_comparisons(worst_case_solution(size_multiplier*N)) / num_comparisons(worst_case_solution(N))
# print(f'For a size increase of {size_multiplier}x, the best-case does {best_case_complexity_multiplyer}x more comparisons')
# print(f'For a size increase of {size_multiplier}x, the worst-case does {worst_case_complexity_multiplyer}x more comparisons')
