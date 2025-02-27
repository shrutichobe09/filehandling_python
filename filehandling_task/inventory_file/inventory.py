class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity, price):
        try:
            if quantity < 0 or price < 0:
                raise ValueError("Quantity and price must be positive values.")
            if name in self.items:
                self.items[name]['quantity'] += quantity
            else:
                self.items[name] = {'quantity': quantity, 'price': price}
        except ValueError as e:
            print(f"Error: {e}")

    def remove_item(self, name, quantity):
        try:
            if name not in self.items:
                raise KeyError(f"Item '{name}' not found in inventory.")
            if self.items[name]['quantity'] < quantity:
                raise ValueError("Insufficient quantity in inventory.")
            
            self.items[name]['quantity'] -= quantity
            if self.items[name]['quantity'] == 0:
                del self.items[name]
        except (KeyError, ValueError) as e:
            print(f"Error: {e}")

    def view_inventory(self):
        if not self.items:
            print("Inventory is empty.")
        else:
            for name, details in self.items.items():
                print(f"{name}: Quantity = {details['quantity']}, Price = {details['price']}")
