from utils.testing import time_plot_count_occurrences

# pylint: disable=pointless-string-statement
"""
The function `count_occurrences` counts the occurrences of
    each integer from `numbers` in `input_list`.

This function is not optimized at all.

* What's the complexity of `count_occurrences`?
    Both `input_list and `numbers` have a non-constant size
       proportional to N. This means looping through either is O(N).
    * Run the script to check your answer.

* Implement `count_occurrences_optimized` so it has a lower
    time-complexity and the same behavior as `count_occurrences`.
    * What's the time complexity of your implementation?
    * Run the script again to check your answer.

HINT 1: Set/get on a dictionary takes O(1).
HINT 2: There are multiple optimizations you can make.
    * The first involves not using expensive list operations.
    * The second (trickier) also involves not having nested for loops. 
"""


def count_occurrences(input_list, numbers):
    """Count the number of occurrences of each integer from numbers
        in the input_list.

    Args:
        input_list (list): A list of integers.
        numbers (list): A list of numbers to count.

    Returns:
        dict: A dictionary from integer to number of occurrences.
            e.g. for numbers = [1, 5], return { 1: 2, 5: 1 }
            means 1 was encountered 2 times and 5 - 1 time
            in `input_list`.
    """
    # Both `input_list and `numbers` have a non-constant size
    #   proportional to N. This means looping through either is O(N).
    occurrences = {}

    # Initialize counts to 0.
    for num in numbers:
        # Accessing an item from a dictionary is O(1)
        occurrences[num] = 0 # O(1)

    for num in numbers:
        input_list_copy = input_list.copy()
        while input_list_copy:
            el = input_list_copy.pop(0)
            if el == num:
                # Count the occurrences of 'num'.
                #   This operation is O(1) as occurrences[num] is O(1).
                occurrences[num] += 1 # O(1)

    return occurrences


def count_occurrences_optimized(input_list, numbers):
    """A faster implementation of count_occurrences"""
    # TODO: Implement so that it behaves like count_occurrences
    #   but with a lower time-complexity.
    ...


# <<< DO NOT CHANGE THE CODE BELOW THIS LINE >>>
if __name__ == '__main__':
    time_plot_count_occurrences(
        count_occurrences,
        count_occurrences_optimized
    )
