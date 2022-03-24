##### MOVE TO DIFFERENT FILE
class Product:
    def __init__(self, product_type, quality, age_order, name, country_of_origin):
        self.product_type = product_type
        self.grade = grade
        self.age = age_order
        self.name = name
        self.country_of_origin = country_of_origin

class MenuItem:
    def __init__(self, meat, vegetable, sauce):
        self.meat = meat
        self.vegetable = vegetable
        self.sauce = sauce
        self.grade = min([self.meat.grade, self.vegetable.grade, self.sauce.grade])
        self.countries_of_origin = [self.meat.country_of_origin, self.vegetable.country_of_origin, self.sauce.country_of_origin]

<O(N^3) inefficient code that can be made O(N log N)>
def build_menu(products):
    meats = products.meats
    vegetables = products.vegetables
    sauces = products.sauces
    # Build items from equal age_order meat, vegetable, sauce
    menu_items = []
    for meat in meats:
        for vegetable in vegetables:
            for sauce in sauces:
                if meat.age_order == vegetable.age_order == sauce.age_order:
                    menu_item = MenuItme(meat, vegetable, sauce)
                    menu_items.append(menu_item)
    return menu_items

<O(N^2) inefficient code that can be made O(N)>
def get_item_to_display(menu_items, country):
    # Sort in descending order according to the grade of the chosen product type
    sorted_menu_items = selection_sort(menu_items, key=lambda item: item.get(product_type).grade)
    item_to_display = sorted_menu_items[0]
    return item_to_display

# DO NOT EDIT BELOW THIS LINE
def restaurant(products, countries):
    N = len(products)
    K = len(countries)
    menu_items = build_menu(products)
    for country in countries:
        # Get only items that have an ingredients from the country
        filtered_menu_items = [item for item in menu_items if country in item.countries_of_origin]
        # Get the item of best grade which has an ingredient from the country
        item_to_display = get_item_to_display(filtered_menu_items, country)
        print("The item to display for " + country + " is " + item_to_display.name)
