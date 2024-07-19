from functions import *

menu_options = '''
1. See recipes \t\t\t2. Create recipe
3. Create category\t\t4. Delete recipe
5. Delete catedory\t\t6. Exit
'''

order = 0

while order != 6:
    cat_dir = Path(os.getcwd()) / 'Recetas'
    print(f'Welcome! The path to the recipes directory is: {cat_dir}')
    print(f'Number of recipes: {len(list(Path(cat_dir).glob("**/*.txt")))}')
    order = select_option(menu_options)

    match order:
        case 1:
            print('Categories:')
            category = select_cat(get_cat(cat_dir))
            recipes_dir = cat_dir / category

            recipe_name = select_recipe(get_recipe(recipes_dir))
            recipe_path = recipes_dir / (recipe_name + '.txt')
            recipe_file = open(recipe_path)
            print(recipe_file.read())
            recipe_file.close()
            press_q()

        case 2:
            print('Recipes:')
            category = select_cat(get_cat(cat_dir))
            recipes_dir = Path(cat_dir) / category
            create_recipe(recipes_dir)

            press_q()

        case 3:
            create_category(cat_dir)
            press_q()

        case 4:
            print('Categories:')
            category = select_cat(get_cat(cat_dir))
            recipes_dir = cat_dir / category

            recipe_name = select_recipe(get_recipe(recipes_dir))
            recipe_path = recipes_dir / (recipe_name + '.txt')
            delete_recipe(recipe_path)
            press_q()

        case 5:
            print('What category do you want to delete?:')
            category = select_cat(get_cat(cat_dir))
            cat_dir = cat_dir / category
            delete_category(cat_dir)
            press_q()

        case 6:
            print('Good bye!')

