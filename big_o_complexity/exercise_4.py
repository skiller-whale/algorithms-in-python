# PART A

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

def find_duplicates(unsorted_list):
    sorted_list = sorted(unsorted_list) # O(N log N)
    have_duplicates = set()
    previous_el = None
    for el in sorted_list:
        # TODO: Utilise the fact the same elements will be adjacent
        pass
    return have_duplicates
