import mysql.connector as mysql


# Establish a connection to the MySQL database
def connect_to_db():
    return mysql.connect(
        host="localhost",
        user="root",
        password="Magic123",
        database="shop"
    )


# View Products from the database
def view_products():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT productID, productName, price FROM Products")
    products = cursor.fetchall()

    result = "Available Products:\n"
    for product in products:
        result += f"{product[0]} *{product[1]} * £{product[2]:.2f}\n"

    cursor.close()
    conn.close()
    return result


# Add to Cart
def add_to_cart(product_id, quantity):
    conn = connect_to_db()
    cursor = conn.cursor()

    # Fetch product details
    cursor.execute("SELECT productName, price, stock FROM Products WHERE productID = %s", (product_id,))
    product = cursor.fetchone()

    if not product:
        cursor.close()
        conn.close()
        return "Product not found."

    product_name, price, stock = product
    if stock < quantity:
        cursor.close()
        conn.close()
        return f"Insufficient stock. Available: {stock}"

    # Insert transaction into CartTransactions
    total_price = price * quantity
    cursor.execute(
        "INSERT INTO CartTransactions (productID, quantity, totalPrice) VALUES (%s, %s, %s)",
        (product_id, quantity, total_price)
    )

    # Update stock in Products
    cursor.execute(
        "UPDATE Products SET stock = stock - %s WHERE productID = %s",
        (quantity, product_id)
    )

    conn.commit()
    cursor.close()
    conn.close()
    return f"Added {quantity} {product_name}(s) to the cart."


# View Cart
def view_cart():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT Products.productName, CartTransactions.quantity, Products.price, CartTransactions.totalPrice
        FROM CartTransactions
        JOIN Products ON CartTransactions.productID = Products.productID
    """)
    cart_items = cursor.fetchall()

    result = "Shopping Cart:\n"
    total = 0
    for item in cart_items:
        result += f"{item[0]}, £{item[2]:.2f} * {item[1]} = £{item[3]:.2f}\n"
        total += item[3]

    result += f"                 Total: £{total:.2f}\n"
    cursor.close()
    conn.close()
    return result


# Checkout
def checkout():
    conn = connect_to_db()
    cursor = conn.cursor()

    # Clear all transactions from CartTransactions
    cursor.execute("DELETE FROM CartTransactions")
    conn.commit()

    cursor.close()
    conn.close()
    return "Thank you for shopping with us! Your cart is now empty."


# Menu
def menu():
    while True:
        print("\nWelcome to the Shopping System!")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print(view_products())
        elif choice == "2":
            product_id = int(input("Enter the product ID: "))
            quantity = int(input("Enter the quantity: "))
            print(add_to_cart(product_id, quantity))
        elif choice == "3":
            print(view_cart())
        elif choice == "4":
            print(checkout())
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the menu2

menu()
