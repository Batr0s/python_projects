from os import system
import os
from pathlib import Path
import keyboard


def select_option(menu_options):
    # Forces the user to select an option and write it in the correct format.
    # Returns the option selected
    order = 'x'
    while not order.isnumeric() or int(order) not in range(1, 7):
        print(menu_options)
        order = input('Select the option (write the number): ')
        if not order.isnumeric() or int(order) not in range(1, 7):
            system('cls')
            print('Invalid input. Please enter a number from 1 to 6.')
    return int(order)


# CATEGORIES


def select_cat(cat_dir):
    # Forces the user to select a category and write it in the correct format.
    categories = get_cat(cat_dir)
    option = 'x'
    while not option.isnumeric() or int(option) not in range(1, len(categories)+1):
        show_cat(categories)
        option = input('Select the category (write the number): ')
        if not option.isnumeric() or int(option) not in range(1, len(categories)):
            system('cls')
            print(f'Invalid input. Please enter a number from 1 to {len(categories)}.')
    print('*' * 50)
    return cat_dir / categories[int(option)]


def get_cat(recipe_dir):
    # Iterates the recipes directory and stores the data in a variable (a dictionaire)
    # Returns a dictionary with keys as number associated to the category and value as the name of the cat.
    cat_dict = dict()
    x = 1
    for item in recipe_dir.iterdir():
        cat_dict[x] = item.name
        x += 1
    return cat_dict


def show_cat(categories):
    # Shows in the console the food categories
    my_str = ''
    for num, cat in categories.items():
        if num % 2 == 1:
            my_str = str(num) + ': ' + cat
        else:
            my_str += '\t\t' + str(num) + ': ' + cat
            print(my_str)
    if len(categories) % 2 == 1:
        print(my_str)


def create_category(cat_dir):
    cat_name = input('Category name: ')
    os.mkdir(Path(cat_dir / cat_name))


def delete_category(category_path):
    os.rmdir(category_path)


# RECIPES

def read_recipe(recipes_dir, recipe_name):
    recipe_path = recipes_dir / (recipe_name + '.txt')
    recipe_file = open(recipe_path)
    print(recipe_file.read())
    recipe_file.close()

def select_recipe(recipe_dir):
    # Forces the user to select a recipe and write it in the correct format.
    recipes = get_recipe(recipe_dir)
    if len(recipes) != 0:
        option = 'x'
        while not option.isnumeric() or int(option) not in range(1, len(recipes)+1):
            show_recipes(recipes)
            option = input('\nSelect the recipe (write the number): ')
            if not option.isnumeric() or int(option) not in range(1, len(recipes)):
                system('cls')
                print(f'Invalid input. Please enter a number from 1 to {len(recipes)}.')
        print('*' * 50)
        return recipes[int(option)]
    else:
        print('Empty category')
        return 0


def get_recipe(recipe_dir):
    # Returns a dictionary with keys as number associated to the recipe and value as the name of the recipe.
    cat_dict = dict()
    x = 1
    for item in recipe_dir.iterdir():
        ruta = Path(recipe_dir / item.name)
        cat_dict[x] = ruta.stem
        x += 1
    return cat_dict


def show_recipes(recipes):
    # Shows in the console all the recipes name
    my_str = ''
    for num, cat in recipes.items():
        if num % 2 == 1:
            my_str = str(num) + ': ' + cat
        else:
            my_str += '\t' + str(num) + ': ' + cat
            print(my_str)
    if len(recipes) % 2 == 1:
        print(my_str)


def create_recipe(recipes_dir):
    recipe_name = (input('Escribe nombre de la receta: ')) + '.txt'
    new_file = open(Path(recipes_dir) / recipe_name, 'w')
    recipe_description = input('Descripción de la receta: ')
    new_file.write(recipe_description)


def delete_recipe(recipes_dir, recipe_name):
    recipe_path = recipes_dir / (recipe_name + '.txt')
    os.remove(recipe_path)


def press_q():
    # Waits until the user presses 'q' keyboard and clears the console
    # The purpose of this is to give some time the user to read the recipe before going to the home menu.
    print("Press 'q' to return home.")
    while True:
        if keyboard.is_pressed('q'):
            system('cls')
            break

