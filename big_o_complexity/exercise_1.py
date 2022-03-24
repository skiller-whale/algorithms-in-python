def calculate_calories(meat_calories_list, vegetable_calories_list, rice_base_calories):
    N = len(meat_calories_list)
    M = len(vegetable_calories_list)
    meal_calories = [[0 for j in range(M)] for i in range(N)]
    for i in range(N):
        for j in range(M):
            meal_calories[i][j] = meat_calories_list[i] + vegetable_calories_list[j] + rice_base_calories
    return meal_calories
