# import tkinter as tk
# from cart import ShoppingCart
#
#
# class ShoppingCartApp(tk.Tk):
#     def __init__(self, data_manager):
#         super().__init__()
#         self.title("Shopping Cart")
#         self.geometry("400x400")
#         self.data_manager = data_manager
#         self.shopping_cart = ShoppingCart()
#         self.load_cart_data()
#
#         self.welcome_screen()
#
#     def load_cart_data(self):
#         cart_data = self.data_manager.load_cart_data()
#         for item, count in cart_data.items():
#             self.shopping_cart.add_item(item, count)
#
#     def welcome_screen(self):
#         self.label = tk.Label(self, text="Welcome to Python Cafe ! \n \n Would you like to place an order?",
#                               font=("Arial", 21))
#         self.label.pack(pady=20)
#
#         self.yes_button = tk.Button(self, text="Yes, please", command=self.show_order_screen)
#         self.yes_button.pack(pady=10)
#
#         self.no_button = tk.Button(self, text="No, thank you", command=self.show_checkout_screen)
#         self.no_button.pack()
#
#     def show_order_screen(self):
#         self.clear_screen()
#         self.label = tk.Label(self, text="Choose an item to order:", font=("Arial", 21))
#         self.label.pack(pady=20)
#
#         self.cookie_button = tk.Button(self, text="Cookie", command=self.show_cookie_screen)
#         self.cookie_button.pack(pady=10)
#
#         self.sandwich_button = tk.Button(self, text="Sandwich", command=self.show_sandwich_screen)
#         self.sandwich_button.pack(pady=10)
#
#         self.drink_button = tk.Button(self, text="Drink", command=self.show_drink_screen)
#         self.drink_button.pack(pady=10)
#
#         self.side_button = tk.Button(self, text="Side", command=self.show_side_screen)
#         self.side_button.pack(pady=10)
#
#         self.checkout_button = tk.Button(self, text="I'm ready to check out", command=self.show_checkout_screen,
#                                          font=("Arial", 14))
#         self.checkout_button.pack(pady=25)
#
#     def show_cookie_screen(self):
#         self.clear_screen()
#         self.label = tk.Label(self, text="Choose a cookie:", font=("Arial", 21))
#         self.label.pack(pady=20)
#
#         self.choc_chip_button = tk.Button(self, text="Chocolate Chip ($1.50)",
#                                           command=self.add_to_cart("Chocolate Chip"))
#         self.choc_chip_button.pack(pady=10)
#
#         self.snickerdoodle_button = tk.Button(self, text="Snickerdoodle ($1.50)",
#                                               command=self.add_to_cart("Snickerdoodle"))
#         self.snickerdoodle_button.pack(pady=10)
#
#         self.back_button = tk.Button(self, text="Back", command=self.show_order_screen)
#         self.back_button.pack(pady=25)
#
#         self.checkout_button = tk.Button(self, text="I'm ready to check out", command=self.show_checkout_screen)
#         self.checkout_button.pack(pady=5)
#
#     def show_sandwich_screen(self):
#         self.clear_screen()
#         self.label = tk.Label(self, text="Choose a sandwich:", font=("Arial", 21))
#         self.label.pack(pady=20)
#
#         self.turkey_button = tk.Button(self, text="Turkey ($7.99)", command=self.add_to_cart("Turkey"))
#         self.turkey_button.pack(pady=10)
#
#         self.ham_button = tk.Button(self, text="Ham ($7.99)", command=self.add_to_cart("Ham"))
#         self.ham_button.pack(pady=10)
#
#         self.caprese_button = tk.Button(self, text="Caprese ($6.99)", command=self.add_to_cart("Caprese"))
#         self.caprese_button.pack(pady=10)
#
#         self.back_button = tk.Button(self, text="Back", command=self.show_order_screen)
#         self.back_button.pack(pady=25)
#
#         self.checkout_button = tk.Button(self, text="I'm ready to check out", command=self.show_checkout_screen)
#         self.checkout_button.pack(pady=5)
#
#     def show_drink_screen(self):
#         self.clear_screen()
#         self.label = tk.Label(self, text="Choose a drink:", font=("Arial", 21))
#         self.label.pack(pady=20)
#
#         self.water_button = tk.Button(self, text="Water ($1.00)", command=self.add_to_cart("Water"))
#         self.water_button.pack(pady=10)
#
#         self.soda_button = tk.Button(self, text="Soda ($1.75)", command=self.add_to_cart("Soda"))
#         self.soda_button.pack(pady=10)
#
#         self.lemonade_button = tk.Button(self, text="Lemonade ($1.50)", command=self.add_to_cart("Lemonade"))
#         self.lemonade_button.pack(pady=10)
#
#         self.back_button = tk.Button(self, text="Back", command=self.show_order_screen)
#         self.back_button.pack(pady=25)
#
#         self.checkout_button = tk.Button(self, text="I'm ready to check out", command=self.show_checkout_screen)
#         self.checkout_button.pack(pady=5)
#
#     def show_side_screen(self):
#         self.clear_screen()
#         self.label = tk.Label(self, text="Choose a side:", font=("Arial", 21))
#         self.label.pack(pady=20)
#
#         self.soup_button = tk.Button(self, text="Soup ($3.25)", command=self.add_to_cart("Soup"))
#         self.soup_button.pack(pady=10)
#
#         self.salad_button = tk.Button(self, text="Salad ($3.25)", command=self.add_to_cart("Salad"))
#         self.salad_button.pack(pady=10)
#
#         self.back_button = tk.Button(self, text="Back", command=self.show_order_screen)
#         self.back_button.pack(pady=25)
#
#         self.checkout_button = tk.Button(self, text="I'm ready to check out", command=self.show_checkout_screen)
#         self.checkout_button.pack(pady=5)
#
#     def add_to_cart(self, item):
#         def inner_func():
#             self.shopping_cart.add_item(item)
#             print(f"{item} added to cart.")
#
#         return inner_func
#
#     def show_checkout_screen(self):
#         self.clear_screen()
#         self.label = tk.Label(self, text="Shopping Cart:", font=("Arial", 21))
#         self.label.pack(pady=20)
#
#         cart_text = self.generate_cart_text()
#         self.cart_label = tk.Label(self, text=cart_text, pady=20)
#         self.cart_label.pack()
#
#         total_cost = self.shopping_cart.calculate_total_cost()
#         self.total_label = tk.Label(self, text=f"Total Cost: ${total_cost:.2f}")
#         self.total_label.pack()
#
#         self.back_button = tk.Button(self, text="Back", command=self.show_order_screen)
#         self.back_button.pack()
#
#     def generate_cart_text(self):
#         cart_text = ""
#         for item, count in self.shopping_cart.get_cart_items():
#             subtotal = self.shopping_cart.get_subtotal(item)
#             cart_text += f"{item} x {count} = ${subtotal:.2f}\n"
#         return cart_text
#
#     def clear_screen(self):
#         for widget in self.winfo_children():
#             widget.destroy()
