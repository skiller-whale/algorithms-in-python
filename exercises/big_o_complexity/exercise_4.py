# PART 1
# * What's the complexity class of find_duplicates_naive?
def find_duplicates_naive(unsorted_list):
    N = len(unsorted_list)
    have_duplicates = set()
    for i in range(N):
        # Look only for elements to the right of this one
        for j in range(i+1, N):
            if unsorted_list[i] == unsorted_list[j]:
                have_duplicates.add(unsorted_list[i]) # O(1) time complexity
    return have_duplicates

# PART B
# * Implement a more efficient find_duplicates functions using `sorted`.
# * What's the complexity class of your code?
def find_duplicates(unsorted_list):
    sorted_list = sorted(unsorted_list) # O(N log N)
    have_duplicates = set() # O(1)
    previous_el = None # O(1)
    for el in sorted_list:
        # TODO: Utilise the fact the same elements will be adjacent
        pass
    return have_duplicates
