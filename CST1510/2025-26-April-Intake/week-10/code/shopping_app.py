from tkinter import *
from tkinter import messagebox

def create_gui():
    def view_products():
        # Placeholder functionality
        products_text.delete(1.0, END)
        products_text.insert(END, "Product List:\n1. Product A\n2. Product B\n3. Product C")

    def add_to_cart():
        product_id = product_id_entry.get()
        quantity = quantity_entry.get()
        if not product_id or not quantity.isdigit():
            messagebox.showerror("Input Error", "Please provide valid product ID and quantity.")
            return
        # Placeholder for adding to cart
        messagebox.showinfo("Add to Cart", f"Added Product ID {product_id} (Quantity: {quantity}) to cart.")

    def view_cart():
        # Placeholder for viewing the cart
        cart_text.delete(1.0, END)
        cart_text.insert(END, "Shopping Cart:\n1. Product A x2\n2. Product B x1\nTotal: $30.00")

    def checkout():
        checkout_choice = messagebox.askyesno("Checkout", "Would you like to checkout?")
        if checkout_choice:
            # Placeholder for checkout process
            messagebox.showinfo("Checkout", "Checkout successful. Thank you for shopping!")
        else:
            messagebox.showinfo("Checkout", "Checkout canceled.")

    def exit_app():
        root.quit()

    # Initialize the main window
    root = Tk()
    root.title("Shopping System")
    root.geometry("800x600")

    # Left frame for products
    left_frame = LabelFrame(root, text="Products", bg="light grey", padx=10, pady=10)
    left_frame.grid(row=0, column=0, padx=10, pady=10)

    products_text = Text(left_frame, width=40, height=20)
    products_text.pack()

    view_products_button = Button(left_frame, text="View Products", command=view_products)
    view_products_button.pack(pady=5)

    product_id_label = Label(left_frame, text="Product ID:")
    product_id_label.pack()

    product_id_entry = Entry(left_frame)
    product_id_entry.pack()

    quantity_label = Label(left_frame, text="Quantity:")
    quantity_label.pack()
    quantity_entry = Entry(left_frame)
    quantity_entry.pack()

    add_to_cart_button = Button(left_frame, text="Add to Cart", command=add_to_cart)
    add_to_cart_button.pack(pady=5)

    # Right frame for cart and checkout
    right_frame = LabelFrame(root, text="Cart & Checkout", bg="light grey", padx=10, pady=10)
    right_frame.grid(row=0, column=1, padx=10, pady=10)

    cart_text = Text(right_frame, width=40, height=15)
    cart_text.pack()

    view_cart_button = Button(right_frame, text="View Cart", command=view_cart)
    view_cart_button.pack(pady=5)

    checkout_button = Button(right_frame, text="Checkout", command=checkout)
    checkout_button.pack(pady=5)

    exit_button = Button(right_frame, text="Exit", command=exit_app)
    exit_button.pack(pady=5)

    # Run the main loop
    root.mainloop()


# Run the GUI
if __name__ == "__main__":
    create_gui()
