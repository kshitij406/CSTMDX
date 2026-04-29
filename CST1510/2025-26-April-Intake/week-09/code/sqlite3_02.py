# Import SQLite3 library
# This library allows Python to interact with SQLite databases.
import sqlite3


# Reconnect to the SQLite database
conn = sqlite3.connect('shop.db')
cursor = conn.cursor()

# Insert sample data into the Products table
products = [
    ('Sneakers', 49.99, 10),
    ('Backpack', 29.99, 15),
    ('Water Bottle', 9.99, 20),
    ('Laptop', 799.99, 5),
    ('Smartphone', 599.99, 8),
    ('Headphones', 99.99, 25)
]

# Insert data using executemany for bulk insertion
cursor.executemany("""
INSERT INTO Products (productName, price, stock)
VALUES (?, ?, ?)
""", products)

# Commit changes and close the connection
conn.commit()
cursor.close()
conn.close()

print("Sample data inserted successfully into the Products table.")
