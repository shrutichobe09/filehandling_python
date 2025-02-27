# main.py

from inventory_file.inventory import Inventory
from inventory_file.transaction import Transaction

def main():
    inventory = Inventory()
    transaction = Transaction(inventory)
    
    while True:
        print("\n1. Add Item")
        print("2. Remove Item")
        print("3. View Inventory")
        print("4. View Transaction History")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            try:
                name = input("Enter item name: ")
                quantity = int(input("Enter quantity: "))
                price = float(input("Enter price: "))
                transaction.add_transaction('add', name, quantity, price)
            except ValueError:
                print("Error: Invalid input for quantity or price.")
                
        elif choice == '2':
            try:
                name = input("Enter item name to remove: ")
                quantity = int(input("Enter quantity to remove: "))
                transaction.add_transaction('remove', name, quantity)
            except ValueError:
                print("Error: Invalid input for quantity.")
                
        elif choice == '3':
            inventory.view_inventory()
            
        elif choice == '4':
            transaction.view_transaction_history()
            
        elif choice == '5':
            print("Exiting inventory system.")
            break
            
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
