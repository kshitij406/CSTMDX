# Import the MySQL connector library
# This library allows Python to interact with a MySQL database.
import mysql.connector as mysql

# Establish a connection to the MySQL server
# Specify the host (server), user credentials, and the target database.
conn = mysql.connect(
    host="localhost",      # The server where the database is hosted; "localhost" refers to the local machine.
    user="root",           # The username for the MySQL database; here, it is "root".
    password="Magic123",   # The password for the root user account.
    database="shop"        # The name of the database to connect to.
)

# Create a cursor object to execute SQL queries
# The cursor acts as a pointer that helps execute and fetch query results.
cursor = conn.cursor()

# Define the SQL query to delete a product where productID = 2
query = "DELETE FROM Products WHERE productID = %s"

# Define the ID of the product(s) to delete
values = (2,)

# Execute the query
cursor.execute(query, values)

# Commit the transaction to save changes in the database
conn.commit()

# Confirm the number of records deleted
print(f"Deleted {cursor.rowcount} record(s) from the Products table.")

# Close the cursor and connection to free up resources
cursor.close()
conn.close()

# Note: This script deletes a product with productID = 2 from the Products table in the "shop" database.
