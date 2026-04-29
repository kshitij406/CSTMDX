import sqlite3
# Reconnect to the SQLite database
conn = sqlite3.connect('shop.db')
cursor = conn.cursor()

# Query products with price > 40
cursor.execute("SELECT * FROM Products WHERE price > ?", (40,))
products = cursor.fetchall()

# Print the results
print("Products with Price > 40:")
print("----------------------------------------------------")
print("| productID | productName     | price   | stock   |")
print("----------------------------------------------------")
for product in products:
    print(f"| {product[0]:<9} | {product[1]:<15} | {product[2]:<7.2f} | {product[3]:<7} |")
print("----------------------------------------------------")

# Close the connection
cursor.close()
conn.close()
