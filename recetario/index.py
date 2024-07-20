from functions import *

menu_options = '''
1. See recipes \t\t\t2. Create recipe
3. Create category\t\t4. Delete recipe
5. Delete catedory\t\t6. Exit
'''

order = 0

while order != 6:
    cat_dir = Path(os.getcwd()) / 'Recetas'
    print(f'Welcome to the recipe manager! \nThe recipes are inside: {cat_dir}')
    print(f'Number of recipes: {len(list(Path(cat_dir).glob("**/*.txt")))}')
    order = select_option(menu_options)

    match order:
        case 1:
            print('Categories:')
            recipes_dir = select_cat(cat_dir)

            recipe_name = select_recipe(recipes_dir)
            if recipe_name != 0:
                read_recipe(recipes_dir, recipe_name)
            press_q()

        case 2:
            print('Recipes:')
            recipes_dir = select_cat(cat_dir)
            create_recipe(recipes_dir)

            press_q()

        case 3:
            create_category(cat_dir)
            press_q()

        case 4:
            print('Categories:')
            recipes_dir = select_cat(cat_dir)

            recipe_name = select_recipe(recipes_dir)
            if recipe_name != 0:
                delete_recipe(recipes_dir, recipe_name)
            press_q()

        case 5:
            print('What category do you want to delete?:')
            recipes_dir = select_cat(cat_dir)
            delete_category(recipes_dir)
            press_q()

        case 6:
            print('Good bye!')

