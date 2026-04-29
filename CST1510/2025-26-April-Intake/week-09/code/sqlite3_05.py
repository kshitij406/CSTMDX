import sqlite3
# Reconnect to the SQLite database
conn = sqlite3.connect('shop.db')
cursor = conn.cursor()

# Delete the product with productID = 2
cursor.execute("DELETE FROM Products WHERE productID = ?", (2,))

# Commit changes and confirm the deletion
conn.commit()
print(f"Deleted {cursor.rowcount} record(s).")

# Close the connection
cursor.close()
conn.close()
