# Import SQLite3 library
# This library allows Python to interact with SQLite databases.
import sqlite3

# Establish a connection to SQLite and create a database file named 'shop.db'
# If 'shop.db' does not exist, it will be created.
conn = sqlite3.connect('shop.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the Products table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Products (
    productID INTEGER PRIMARY KEY AUTOINCREMENT,  -- Unique ID for each product
    productName TEXT NOT NULL,                    -- Name of the product
    price REAL NOT NULL,                          -- Price of the product
    stock INTEGER NOT NULL                        -- Stock quantity available
)
""")

# Commit changes and close the connection
conn.commit()
cursor.close()
conn.close()

print("Database and Products table created successfully.")
