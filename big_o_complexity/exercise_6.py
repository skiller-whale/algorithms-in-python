def sleep_food_off(current_weight): # O(current_weight)
    while current_weight > 0:
        current_weight -= 1
    return current_weight

def eat_a_fish(current_weight, capacity): #O(1) or O(1) calls to sleep_food_off
    current_weight += 1
    if current_weight == capacity:
        capacity *= 2
        current_weight = sleep_food_off(current_weight)
    return current_weight, capacity

def devour_ocean(N): # O(N) calls to eat_a_fish
    current_weight = 0
    capacity = 1
    for i in range(N):
        current_weight, capacity = eat_a_fish(current_weight, capacity)
