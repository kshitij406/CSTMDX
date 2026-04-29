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

# Define the SQL query to select all products where the price is greater than 40
query = "SELECT * FROM Products WHERE price > 40"

# Execute the query
cursor.execute(query)

# Fetch all rows returned by the query
products = cursor.fetchall()

# Print the data in a readable format
print("Products with Price > 40:")
print("----------------------------------------------------")
print("| productID | productName     | price   | stock   |")
print("----------------------------------------------------")
for row in products:
    print(f"| {row[0]:<9} | {row[1]:<15} | {row[2]:<7} | {row[3]:<7} |")
print("----------------------------------------------------")

# Close the cursor and connection to free up resources
cursor.close()
conn.close()

# Note: This script retrieves all products where the price is greater than 40 from the Products table in the "shop" database.
