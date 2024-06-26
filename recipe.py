# import sqlite3

# def create_tables():
#     connection = sqlite3.connect('recipes.db')
#     cursor = connection.cursor()

#     cursor.execute('''CREATE TABLE IF NOT EXISTS recipes (
#                         id INTEGER PRIMARY KEY,
#                         name TEXT
#                     )''')

#     cursor.execute('''CREATE TABLE IF NOT EXISTS ingredients (
#                         id INTEGER PRIMARY KEY,
#                         name TEXT
#                     )''')

#     cursor.execute('''CREATE TABLE IF NOT EXISTS recipe_ingredients (
#                         recipe_id INTEGER,
#                         ingredient_id INTEGER,
#                         quantity TEXT,
#                         FOREIGN KEY(recipe_id) REFERENCES recipes(id),
#                         FOREIGN KEY(ingredient_id) REFERENCES ingredients(id),
#                         PRIMARY KEY (recipe_id, ingredient_id)
#                     )''')

#     connection.commit()
#     connection.close()

# def add_recipe(name):
#     connection = sqlite3.connect('recipes.db')
#     cursor = connection.cursor()

#     cursor.execute("INSERT INTO recipes (name) VALUES (?)", (name,))
#     recipe_id = cursor.lastrowid

#     connection.commit()
#     connection.close()

#     return recipe_id

# def add_ingredient(name):
#     connection = sqlite3.connect('recipes.db')
#     cursor = connection.cursor()

#     cursor.execute("INSERT INTO ingredients (name) VALUES (?)", (name,))
#     ingredient_id = cursor.lastrowid

#     connection.commit()
#     connection.close()

#     return ingredient_id

# def add_recipe_ingredient(recipe_id, ingredient_id, quantity):
#     connection = sqlite3.connect('recipes.db')
#     cursor = connection.cursor()

#     cursor.execute("INSERT INTO recipe_ingredients (recipe_id, ingredient_id, quantity) VALUES (?, ?, ?)", (recipe_id, ingredient_id, quantity))

#     connection.commit()
#     connection.close()

# def delete_recipe(recipe_id):
#     connection = sqlite3.connect('recipes.db')
#     cursor = connection.cursor()

#     cursor.execute("DELETE FROM recipes WHERE id = ?", (recipe_id,))

#     connection.commit()
#     connection.close()

# def delete_ingredient(ingredient_id):
#     connection = sqlite3.connect('recipes.db')
#     cursor = connection.cursor()

#     cursor.execute("DELETE FROM ingredients WHERE id = ?", (ingredient_id,))

#     connection.commit()
#     connection.close()

# def main():
#     create_tables()

#     while True:
#         print("\n1. Add recipe")
#         print("2. Add ingredient")
#         print("3. Add ingredient to recipe")
#         print("4. Delete recipe")
#         print("5. Delete ingredient")
#         print("0. Exit")

#         choice = input("Enter your choice: ")

#         if choice == "1":
#             name = input("Enter recipe name: ")
#             add_recipe(name)
#         elif choice == "2":
#             name = input("Enter ingredient name: ")
#             add_ingredient(name)
#         elif choice == "3":
#             recipe_id = input("Enter recipe ID: ")
#             ingredient_id = input("Enter ingredient ID: ")
#             quantity = input("Enter quantity: ")
#             add_recipe_ingredient(recipe_id, ingredient_id, quantity)
#         elif choice == "4":
#             recipe_id = input("Enter recipe ID to delete: ")
#             delete_recipe(recipe_id)
#         elif choice == "5":
#             ingredient_id = input("Enter ingredient ID to delete: ")
#             delete_ingredient(ingredient_id)
#         elif choice == "0":
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()
