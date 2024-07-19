from os import system
import os
from pathlib import Path
import keyboard


def select_option(menu_options):
    # Forces the user to select an option and write it in the correct format.
    # Returns the option selected (an int)
    print(menu_options)
    while True:
        try:
            order = int(input('Select the option (write the number): '))
            if order > 6 or order < 1:
                raise ValueError
            break
        except ValueError:
            system('cls')
            print(menu_options)
            print('Invalid input. Please enter a number from 1 to 6.')
    return order


# CATEGORIES


def get_cat(recipe_dir):
    # Iterates the recipes directory and stores the data in a variable (a dictionaire)
    # Returns a dictionary with keys as number associated to the category and value as the name of the cat.
    cat_dict = dict()
    x = 1
    for item in recipe_dir.iterdir():
        cat_dict[x] = item.name
        x += 1
    return cat_dict


def select_cat(categories):
    # Forces the user to select a category and write it in the correct format.
    show_cat(categories)
    while True:
        try:
            option = int(input('Select a category (write the number): '))
            if option > len(categories) or option < 1:
                raise ValueError
            break
        except ValueError:
            system('cls')
            show_cat(categories)
            print(f'Invalid input. Please enter a number from 1 to {len(categories)}.')
    return categories[option]


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


def get_recipe(recipe_dir):
    # Returns a dictionary with keys as number associated to the recipe and value as the name of the recipe.
    cat_dict = dict()
    x = 1
    for item in recipe_dir.iterdir():
        ruta = Path(recipe_dir / item.name)
        cat_dict[x] = ruta.stem
        x += 1
    return cat_dict


def select_recipe(recipes):
    # Forces the user to select a recipe and write it in the correct format.
    show_recipes(recipes)
    while True:
        try:
            option = int(input('Select a recipe (write the number): '))
            if option > len(recipes) or option < 1:
                raise ValueError
            break
        except ValueError:
            system('cls')
            show_recipes(recipes)
            print(f'Invalid input. Please enter a number from 1 to {len(recipes)}.')
    return recipes[option]


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


def delete_recipe(recipe_path):
    os.remove(recipe_path)

def press_q():
    # Waits until the user presses 'q' keyboard and clears the console
    # The purpose of this is to give some time the user to read the recipe before going to the home menu.
    print("Press 'q' to return home.")
    while True:
        if keyboard.is_pressed('q'):
            system('cls')
            break

