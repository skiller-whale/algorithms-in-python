import time
from utils.custom_list import CustomList
from utils.plotting import plot_list_timing

# pylint: disable=pointless-string-statement
"""
* Implement the function `time_list_append` so that it times
    the execution of append operations to the CustomList `custom_list`.

    To time operations, use `time.perf_counter()`, which returns a time
        in seconds since the start of the program. You can subtract the
        return value of `perf_counter()` before and after the call to append.

* Run the script and examine the plot.
    Can you explain the pattern you see?
    What can you say about the time complexity of `append`?
"""

# the items to append to the list
items = range(1, 2 ** 15 + 2, 1)


def time_list_append(items_to_append):
    custom_list = CustomList()
    times = []

    # TODO: Populate `times` with the time
    #   it took for each append from `items_to_append` to `custom_list`
    return times


# <<< DO NOT CHANGE THE CODE BELOW THIS LINE >>>
if __name__ == '__main__':
    # compute append time
    times_custom_list = time_list_append(items)

    # plot timing
    plot_list_timing(times_custom_list)
