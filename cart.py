from collections import defaultdict

class ShoppingCart:
    def __init__(self):
        self._cart = defaultdict(int)

    def clear(self):
        # Use defaultdict instead of a regular dictionary
        self._cart = defaultdict(int)

    def add_item(self, item):
        # Add an item to the cart. If the item is already in the cart, increase its quantity.
        self._cart[item] += 1

    def remove_item(self, item):
        # Remove one quantity of an item from the cart. If the item's quantity becomes zero, it stays in the dictionary.
        if self._cart[item] > 0:
            self._cart[item] -= 1

    def clear_cart(self):
        # Clear the entire cart by clearing the dictionary.
        self._cart.clear()

    def get_cart_items(self):
        # Return all items and their quantities in the cart.
        return self._cart.items()

    def get_subtotal(self, item):
        # Get the subtotal cost of an item by multiplying its quantity with its price.
        price_mapping = {
            "Chocolate Chip": 1.50,
            "Snickerdoodle": 1.50,
            "Turkey": 7.99,
            "Ham": 7.99,
            "Caprese": 6.99,
            "Water": 1.00,
            "Soda": 1.75,
            "Lemonade": 1.50,
            "Soup": 3.25,
            "Salad": 3.25
        }
        return self._cart.get(item, 0) * price_mapping.get(item, 0)

    def calculate_total_cost(self):
        # Calculate the total cost of all items in the cart.
        return sum(self.get_subtotal(item) for item, _ in self._cart.items())
