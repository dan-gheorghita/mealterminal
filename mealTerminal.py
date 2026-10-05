import sqlite3

conn = sqlite3.connect('mealingredients.db', isolation_level=None)

# Create tables
conn.execute('CREATE TABLE IF NOT EXISTS meals (name TEXT) STRICT')
conn.execute('''
    CREATE TABLE IF NOT EXISTS ingredients (
        name TEXT,
        meal_id INTEGER,
        FOREIGN KEY(meal_id) REFERENCES meals(rowid)
    ) STRICT
''')

def add_meal(meal_name, ingredient_list):
    conn.execute('INSERT INTO meals (name) VALUES (?)', (meal_name,))
    meal_id = conn.execute('SELECT rowid FROM meals WHERE name = ?', (meal_name,)).fetchone()[0]
    for ingredient in ingredient_list:
        conn.execute('INSERT INTO ingredients (name, meal_id) VALUES (?, ?)', (ingredient.strip(), meal_id))
    print(f"Meal added: {meal_name}")

def list_ingredients(meal_name):
    rows = conn.execute('''
        SELECT ingredients.name FROM ingredients
        JOIN meals ON meals.rowid = ingredients.meal_id
        WHERE meals.name = ?
    ''', (meal_name,))
    print(f"Ingredients of {meal_name}:")
    for row in rows:
        print(f"  {row[0]}")

def list_meals_with_ingredient(ingredient_name):
    rows = conn.execute('''
        SELECT meals.name FROM meals
        JOIN ingredients ON meals.rowid = ingredients.meal_id
        WHERE ingredients.name = ?
    ''', (ingredient_name,))
    print(f"Meals that use {ingredient_name}:")
    for row in rows:
        print(f"  {row[0]}")

while True:
    user_input = input("> ").strip()
    if user_input.lower() == "quit":
        break
    elif ":" in user_input:
        meal, ingredients = user_input.split(":", 1)
        ingredient_list = [i.strip() for i in ingredients.split(",") if i.strip()]
        add_meal(meal.strip(), ingredient_list)
    else:
        # Check if input is a meal
        meal_exists = conn.execute('SELECT 1 FROM meals WHERE name = ?', (user_input,)).fetchone()
        if meal_exists:
            list_ingredients(user_input)
        else:
            # Check if input is an ingredient
            ingredient_exists = conn.execute('SELECT 1 FROM ingredients WHERE name = ?', (user_input,)).fetchone()
            if ingredient_exists:
                list_meals_with_ingredient(user_input)