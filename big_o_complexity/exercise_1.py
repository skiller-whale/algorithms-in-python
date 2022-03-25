def calculate_calories(meat_calories_list, vegetable_calories_list, rice_base_calories):
    """
    Given a list of the calories contained in various meats and vegetables, computes how much calories
    each possible meal combination would contain (including rice) and stores it in a 2 dimensional list.
    """
    N = len(meat_calories_list)
    M = len(vegetable_calories_list)
    # Initialises the 2D list with zeros
    meal_calories = [[0 for j in range(M)] for i in range(N)]
    for i in range(N):
        for j in range(M):
            # Calculates the calories (including rice) for the meal containing the ith meat and jth vegetable
            meal_calories[i][j] = meat_calories_list[i] + vegetable_calories_list[j] + rice_base_calories
    return meal_calories
