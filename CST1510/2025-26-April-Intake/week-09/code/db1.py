# Import the MySQL connector library
# This library allows Python to interact with a MySQL database.
import mysql.connector as mysql

# Establish a connection to the MySQL server
# Specify the host (server), user credentials, and optionally a database.
conn = mysql.connect(
    host="localhost",      # The server where the database is hosted; "localhost" refers to the local machine.
    user="root",           # The username for the MySQL database; here, it is "root".
    password="Magic123"    # The password for the root user account.
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create a new database if it doesn't already exist
# The first line checks if the database exists; if not, the second line creates it.
cursor.execute("CREATE DATABASE IF NOT EXISTS shop")  # Create a database named "shop"

# Close the cursor to free resources
cursor.close()

# Optional: Close the connection to the database server
conn.close()

# Note: This script only connects to the server and creates a database.
# To work with tables or data, reconnect to the newly created "shop" database in the next steps.
