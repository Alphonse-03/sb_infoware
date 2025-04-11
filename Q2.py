# 2. Python - Process Orders from CSV
# You have received a CSV file (orders.csv) containing new food orders. The file format is:

# DishName, RestaurantName, CustomerName
# Burger, Foodies, Alice
# Pasta, Italian Delight, Bob
# Pizza, Foodies, Charlie

# Python Script Requirements:
# Read the CSV file and insert orders into the Orders table.
# Ensure the dish and restaurant exist in the database before inserting an order.
# Handle missing values and incorrect data formats gracefully.
# If a dish or restaurant does not exist, log the error and skip that order instead of stopping execution.


import psycopg2
from psycopg2 import execute
conn = psycopg2.connect(
    dbname="food_delivery",
    user="username",
    password="password",   
    host="localhost",
    port="5432"
)


cur =conn.cursor()
import csv
with open('abc.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for rows in csvFile:
        dish_name = rows[0]
        restaurant_name = rows[1]
        customer_name = rows[2]
        if dish_name and restaurant_name:
            cur.execute("SELECT d.id FROM Dishes d JOIN Restaurants r ON d.restaurant_id = r.id WHERE d.name = %s AND r.name = %s", (dish_name, restaurant_name))
            dish = cur.fetchone()
            if not customer_name:
                customer_name = "Unknown"
            if dish:
                cur.execute("INSERT INTO Orders (dish_id, customer_name) VALUES (%s, %s)", (dish[0], customer_name))
                conn.commit()
            else:
                print("The given dish doens't exist in the database or the restaurant is not valid.")
        else:
            print("Dish name or restaurant name is missing.")

cur.close()
conn.close()
