spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    name_list = []

    for spicy_food in spicy_foods:
        name_list.append(spicy_food["name"])

    return name_list 

def get_spiciest_foods(spicy_foods):
    result = list()

    for spicy_food in spicy_foods:
        if spicy_food["heat_level"] > 5:
            result.append(spicy_food)

    return result

def print_spicy_foods(spicy_foods):
    for spicy_food in spicy_foods:
        name, cuisine, heat_level = spicy_food.values()
        print(f'{name} ({cuisine}) | Heat Level: {"🌶" * heat_level}')


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for spicy_food in spicy_foods:
        if spicy_food["cuisine"] == cuisine:
            return spicy_food

def print_spiciest_foods(spicy_foods):
    print_spicy_foods(get_spiciest_foods(spicy_foods))

def get_average_heat_level(spicy_foods):
    average_heat_level = 0
    for spicy_food in spicy_foods:
        average_heat_level += spicy_food["heat_level"]

    return int(average_heat_level/len(spicy_foods))

def create_spicy_food(spicy_foods, spicy_food):
    return spicy_foods.append(spicy_food)


# print(print_spiciest_foods(spicy_foods))
# print(get_average_heat_level(spicy_foods))
spicy_food = {
    'name': 'Jerk Chicken',
    'cuisine': 'Jamaican',
    'heat_level': 8
}

create_spicy_food(spicy_foods, spicy_food)
print(spicy_foods)