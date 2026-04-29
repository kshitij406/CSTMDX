import sqlite3
# Reconnect to the SQLite database
conn = sqlite3.connect('shop.db')
cursor = conn.cursor()

# Update the stock of a product with productID = 1
cursor.execute("""
UPDATE Products
SET stock = ?
WHERE productID = ?
""", (20, 1))

# Commit changes and confirm the update
conn.commit()
print(f"Updated {cursor.rowcount} record(s).")

# Close the connection
cursor.close()
conn.close()
