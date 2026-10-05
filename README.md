# mealTerminal.py

**Meal Ingredients Database Management System**

This Python script implements a simple command-line interface for managing a meal ingredients database using SQLite. It allows users to add meals with their corresponding ingredients, list ingredients for a specific meal, and list meals that use a specific ingredient.

**Database Schema**

The database consists of two tables:

1. **meals**: stores the names of meals with a unique `rowid` identifier.
2. **ingredients**: stores the names of ingredients and their corresponding meal identifiers (`meal_id`).

**Functions**

The script defines three functions:

1. **`add_meal`**: takes a `meal_name` and a list of `ingredient_list` as input. It inserts the meal into the `meals` table and then inserts each ingredient into the `ingredients` table with the corresponding meal identifier.
2. **`list_ingredients`**: takes a `meal_name` as input and prints the list of ingredients for that meal by joining the `ingredients` table with