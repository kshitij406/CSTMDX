# Import the MySQL connector library
# This library allows Python to interact with a MySQL database.
import mysql.connector as mysql

# Establish a connection to the MySQL server
# Specify the host (server), user credentials, and optionally a database.
conn = mysql.connect(
    host="localhost",      # The server where the database is hosted; "localhost" refers to the local machine.
    user="root",           # The username for the MySQL database; here, it is "root".
    password="Magic123",   # The password for the root user account.
    database="shop"        # The name of the database to connect to.
)

# Create a cursor object to execute SQL queries
# The cursor acts as a pointer that helps execute and fetch query results.
cursor = conn.cursor()

# Execute the SQL query to create the Products table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Products (
    productID INT AUTO_INCREMENT PRIMARY KEY,
    productName VARCHAR(50) NOT NULL,
    price DECIMAL(7,2) NOT NULL,
    stock INT NOT NULL
)
""")

# Commit the changes (not required for table creation but good practice for write operations)
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

# Note: This script creates a table named "Products" in the "shop" database.
