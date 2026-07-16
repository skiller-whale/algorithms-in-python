from collections import deque
from typing import Deque
import random

def check_for_new_orcas(num_groups):
    if num_groups > 20:
        return []
    new_orcas = []
    for _ in range(10):
        if random.randint(0, 10) < 7:
            new_orcas.append({'group_number': num_groups, 'colour': 'red' if random.randint(0, 1) else 'blue' })
    return new_orcas

def feed(orca, highest_group_number_fed):
    if orca['group_number'] < highest_group_number_fed:
        raise ValueError('Tried to feed an orca from an earlier group')
    highest_group_number_fed = max(highest_group_number_fed, orca['group_number'])
    return highest_group_number_fed


num_groups = 0
highest_group_number_fed = 0
# serving_queue = deque([])
serving_queue = []
while True:
    if len(serving_queue) > 0:
        # TODO: Get the least-recent orca
        hungry_orca = serving_queue.pop()
        highest_group_number_fed = feed(hungry_orca, highest_group_number_fed)
        print(f"Just fed Orca from group {hungry_orca['group_number']}")

    result = check_for_new_orcas(num_groups)
    num_groups += 1
    if result:
        for orca in result:
            # TODO: Add the orca to the deque
            serving_queue.append(orca)
            pass

### Part 2
def check_if_middle_orca_is_red(serving_queue):
    # TODO: Implement this
    pass