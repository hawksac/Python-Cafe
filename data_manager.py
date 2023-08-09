import csv

class DataManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def save_cart_data(self, cart_data):
        with open(self.file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Item', 'Count'])
            for item, count in cart_data.items():
                writer.writerow([item, count])

    def load_cart_data(self):
        cart_data = {}
        try:
            with open(self.file_path, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header row
                for row in reader:
                    item, count = row
                    cart_data[item] = int(count)
        except FileNotFoundError:
            pass
        return cart_data

    def clear_cart_data(self):
        with open(self.file_path, 'w', newline='') as file:
            file.write("")
