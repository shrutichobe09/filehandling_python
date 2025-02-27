# transaction.py

class Transaction:
    def __init__(self, inventory):
        self.inventory = inventory
        self.history = []

    def add_transaction(self, action, name, quantity, price=None):
        try:
            if action == 'add':
                self.inventory.add_item(name, quantity, price)
            elif action == 'remove':
                self.inventory.remove_item(name, quantity)
            else:
                raise ValueError("Invalid action. Must be 'add' or 'remove'.")
            
            transaction_details = {
                'action': action,
                'name': name,
                'quantity': quantity,
                'price': price if price is not None else self.inventory.items.get(name, {}).get('price', None)
            }
            self.history.append(transaction_details)
            print(f"Transaction successful: {action} {quantity} of {name}")
        except Exception as e:
            print(f"Transaction Error: {e}")

    def view_transaction_history(self):
        if not self.history:
            print("No transactions yet.")
        else:
            for transaction in self.history:
                print(transaction)
