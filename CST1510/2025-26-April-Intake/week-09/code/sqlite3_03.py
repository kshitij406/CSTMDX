# Import SQLite3 library
# This library allows Python to interact with SQLite databases.
import sqlite3


# Reconnect to the SQLite database
conn = sqlite3.connect('shop.db')
cursor = conn.cursor()

# Query all products
cursor.execute("SELECT * FROM Products")
products = cursor.fetchall()

# Print the results in a formatted table
print("Products Table Data:")
print("----------------------------------------------------")
print("| productID | productName     | price   | stock   |")
print("----------------------------------------------------")
for product in products:
    print(f"| {product[0]:<9} | {product[1]:<15} | {product[2]:<7.2f} | {product[3]:<7} |")
print("----------------------------------------------------")

# Close the connection
cursor.close()
conn.close()
