import tkinter as tk
import tkinter.messagebox as messagebox
from cart import ShoppingCart

# A custom button class to handle 'Add to Cart' actions, extending the standard tkinter Button.
class AddToCartButton(tk.Button):
    def __init__(self, parent, **kwargs):
        # Setting default configurations. These can be overridden by explicitly providing these in **kwargs.
        kwargs.setdefault('text', 'Add to Cart')
        kwargs.setdefault('bg', '#4CAF50')  # Green background
        kwargs.setdefault('fg', 'black')  # White text
        kwargs.setdefault('relief', 'raised')
        kwargs.setdefault('padx', 10)
        kwargs.setdefault('pady', 5)

        super().__init__(parent, **kwargs)

# A custom button class to define standard appearance, extending the standard tkinter Button.
class CustomButton(tk.Button):
    def __init__(self, parent, **kwargs):
        # Setting default configurations. These can be overridden by explicitly providing these in **kwargs.
        kwargs.setdefault('width', 15)  # set your desired width
        kwargs.setdefault('height', 2)  # set your desired height
        kwargs.setdefault('bg', 'white')  # set the background color to white
        kwargs.setdefault('borderwidth', 3)  # set the border size
        kwargs.setdefault('relief', 'raised')  # set the border type

        super().__init__(parent, **kwargs)

# The main application class that manages the shopping cart interface.
class ShoppingCartApp(tk.Tk):
    # Initialize the app with a given shopping cart
    def __init__(self):
        super().__init__()
        self.title("Shopping Cart")
        self.geometry("400x500")
        self.shopping_cart = ShoppingCart()
        self.welcome_screen()

        # Validation command for the Spinbox
        self.vcmd = (self.register(self.validate_spinbox_input), '%P')
        self.cart_window = None

    def clear_cart(self):
        self.shopping_cart.clear()  # This will call the clear method from the ShoppingCart class
        if self.cart_window:  # Close the cart window if it's open
            self.cart_window.destroy()
            self.cart_window = None
        tk.messagebox.showinfo("Info", "Cart has been cleared!")  # Optionally show a confirmation message
        self.show_order_screen()
    def validate_spinbox_input(self, P):
        if str.isdigit(P) and 1 <= int(P) <= 100:
            return True
        else:
            return False

    # Display a popup window showing the current items in the shopping cart

    def show_cart_popup(self):
        # Destroy existing cart window if one exists
        if self.cart_window is not None:
            self.cart_window.destroy()

        # Initialize a new cart window
        self.cart_window = tk.Toplevel(self)
        self.cart_window.title("Shopping Cart")
        self.cart_window.geometry("400x400+400+30")

        cart_label = tk.Label(self.cart_window, text="Shopping Cart:", font=("Arial", 21))
        cart_label.pack(pady=20)

        cart_text = self.generate_cart_text()
        cart_contents_label = tk.Label(self.cart_window, text=cart_text, pady=20)
        cart_contents_label.pack()

        total_cost = self.shopping_cart.calculate_total_cost()
        total_label = tk.Label(self.cart_window, text=f"Total Cost: ${total_cost:.2f}")
        total_label.pack()

    # Utility method to add an item to the GUI with a spinbox to select quantity and a button to add to cart

    def add_button_with_spinbox(self, item_name, item_display, item_price, y_padding=10):
        frame = tk.Frame(self)
        frame.pack(pady=y_padding)

        label = tk.Label(frame, text=f"{item_display} (${item_price:.2f})", font=("Arial", 14))
        label.pack(side=tk.LEFT, padx=5)

        spinbox = tk.Spinbox(frame, from_=0, to=100, increment=1,
                             validate='key',
                             validatecommand=self.vcmd,
                             font=("Arial", 14),
                             bg="lightgray",
                             fg="black",
                             highlightbackground="white",
                             width=5)
        spinbox.pack(side=tk.LEFT, padx=5)
        spinbox.update_idletasks()
        add_to_cart_btn = AddToCartButton(frame, command=lambda: self.add_to_cart(item_name, spinbox.get()))
        add_to_cart_btn.pack(side=tk.LEFT, padx=5)

        return label, spinbox, add_to_cart_btn

    # Welcome screen displayed on app launch
    def welcome_screen(self):
        self.label = tk.Label(self, text="Welcome to Python Cafe ! \n \n Would you like to place an order?",
                              font=("Arial", 21))
        self.label.pack(pady=20)

        self.yes_button = CustomButton(self, text="Yes, please", command=self.show_order_screen)
        self.yes_button.pack(pady=10)

        self.no_button = CustomButton(self, text="No, thank you", command=self.show_checkout_screen)
        self.no_button.pack()

    # Screen to show different item categories like cookie, sandwich, etc.

    def show_order_screen(self):
        self.clear_screen()
        self.label = tk.Label(self, text="Choose an item to order:", font=("Arial", 21))
        self.label.pack(pady=20)

        self.cookie_button = CustomButton(self, text="Cookie", command=self.show_cookie_screen)
        self.cookie_button.pack(pady=10)

        self.sandwich_button = CustomButton(self, text="Sandwich", command=self.show_sandwich_screen)
        self.sandwich_button.pack(pady=10)

        self.drink_button = CustomButton(self, text="Drink", command=self.show_drink_screen)
        self.drink_button.pack(pady=10)

        self.side_button = CustomButton(self, text="Side", command=self.show_side_screen)
        self.side_button.pack(pady=10)

        self.checkout_button = CustomButton(self, text="Check out", command=self.show_checkout_screen)
        self.checkout_button.pack(pady=25)

    # Screen for cookie selection
    def show_cookie_screen(self):
        self.clear_screen()
        self.label = tk.Label(self, text="Choose a cookie:", font=("Arial", 21))
        self.label.pack(pady=20)

        # Quantity Spinbox for Chocolate Chip
        choc_chip_frame = tk.Frame(self)
        choc_chip_frame.pack(pady=10)

        self.choc_chip_label, self.choc_chip_spinbox, self.choc_chip_add_btn = self.add_button_with_spinbox(
            "Chocolate Chip", "Chocolate Chip", 1.50)
        self.snickerdoodle_button, self.snickerdoodle_spinbox, self.snickerdoodle_add_btn = self.add_button_with_spinbox("Snickerdoodle",
                                                                                             "Snickerdoodle", 1.50)

        self.back_button = CustomButton(self, text="Back", command=self.show_order_screen)
        self.back_button.pack(pady=25)

        self.checkout_button = CustomButton(self, text="Check out", command=self.show_checkout_screen)
        self.checkout_button.pack(pady=5)

        self.clear_cart_button = CustomButton(self, text="Clear Cart", command=self.clear_cart)
        self.clear_cart_button.pack(pady=10)

    # Screen for sandwich selection
    def show_sandwich_screen(self):
        self.clear_screen()
        self.label = tk.Label(self, text="Choose a sandwich:", font=("Arial", 21))
        self.label.pack(pady=20)

        self.turkey_button, self.turkey_spinbox, self.turkey_add_btn = self.add_button_with_spinbox("Turkey", "Turkey", 7.99)
        self.ham_button, self.ham_spinbox, self.ham_add_btn= self.add_button_with_spinbox("Ham", "Ham", 7.99)
        self.caprese_button, self.caprese_spinbox,  self.caprese_add_btn = self.add_button_with_spinbox("Caprese", "Caprese", 6.99)


        self.back_button = CustomButton(self, text="Back", command=self.show_order_screen)
        self.back_button.pack(pady=25)

        self.checkout_button = CustomButton(self, text="Check out", command=self.show_checkout_screen)
        self.checkout_button.pack(pady=5)

        self.clear_cart_button = CustomButton(self, text="Clear Cart", command=self.clear_cart)
        self.clear_cart_button.pack(pady=10)

    # Screen for drink selection
    def show_drink_screen(self):
        self.clear_screen()
        self.label = tk.Label(self, text="Choose a drink:", font=("Arial", 21))
        self.label.pack(pady=20)

        self.water_button, self.water_spinbox, self.water_add_btn= self.add_button_with_spinbox("Water", "Water", 1.00)
        self.soda_button, self.soda_spinbox, self.soda_add_btn = self.add_button_with_spinbox("Soda", "Soda", 1.75)
        self.lemonade_button, self.lemonade_spinbox, self.lemonade_add_btn = self.add_button_with_spinbox("Lemonade", "Lemonade", 1.50)

        self.back_button = CustomButton(self, text="Back", command=self.show_order_screen)
        self.back_button.pack(pady=25)

        self.checkout_button = CustomButton(self, text="Check out", command=self.show_checkout_screen)
        self.checkout_button.pack(pady=5)

        self.clear_cart_button = CustomButton(self, text="Clear Cart", command=self.clear_cart)
        self.clear_cart_button.pack(pady=10)

    # Screen for side selection
    def show_side_screen(self):
        self.clear_screen()
        self.label = tk.Label(self, text="Choose a side:", font=("Arial", 21))
        self.label.pack(pady=20)

        self.soup_button, self.soup_spinbox, self.soup_add_btn = self.add_button_with_spinbox("Soup", "Soup", 3.25)
        self.salad_button, self.salad_spinbox, self.salad_add_btn = self.add_button_with_spinbox("Salad", "Salad", 3.25)


        self.back_button = CustomButton(self, text="Back", command=self.show_order_screen)
        self.back_button.pack(pady=25)

        self.checkout_button = CustomButton(self, text="Check out", command=self.show_checkout_screen)
        self.checkout_button.pack(pady=5)

        self.clear_cart_button = CustomButton(self, text="Clear Cart", command=self.clear_cart)
        self.clear_cart_button.pack(pady=10)

    def show_checkout_screen(self):
        self.clear_screen()
        self.label = tk.Label(self, text="Shopping Cart:", font=("Arial", 21))
        self.label.pack(pady=20)

        cart_text = self.generate_cart_text()
        self.cart_label = tk.Label(self, text=cart_text, pady=20)
        self.cart_label.pack()

        total_cost = self.shopping_cart.calculate_total_cost()
        self.total_label = tk.Label(self, text=f"Total Cost: ${total_cost:.2f}")
        self.total_label.pack()

        self.back_button = CustomButton(self, text="Back", command=self.show_order_screen)
        self.back_button.pack()

        self.pay_now_button = CustomButton(self, text="Pay Now", command=self.pay_now)
        self.pay_now_button.pack(pady=5)

    def pay_now(self):
        # Replace this with your payment processing logic
        print("Processing payment... Thank you for your purchase!")

    # Create a textual representation of the cart's content
    def generate_cart_text(self):
        cart_text = ""
        for item, count in self.shopping_cart.get_cart_items():  # Remove the unnecessary .items() here
            subtotal = self.shopping_cart.get_subtotal(item)
            cart_text += f"{item} x {count} = ${subtotal:.2f}\n"
        return cart_text

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

    def add_to_cart(self, item, quantity_str):
        # Check if the integer is between 1 and 100
        if not quantity_str.isdigit() or not (1 <= int(quantity_str) <= 100):
            messagebox.showerror("Invalid Input", "Please enter a valid number between 1-100.")
            return

        quantity = int(quantity_str)
        for _ in range(quantity):
            self.shopping_cart.add_item(item)
        print(f"{quantity} x {item} added to cart.")
        self.show_cart_popup()


