import json
import os
from datetime import datetime

class StockControl:
    def __init__(self):
        self.file_path = 'stock.json'
        self.stock = self.load_stock()

    def load_stock(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return json.load(file)
        return {'items': []}

    def save_stock(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.stock, file, indent=2)

    def add_item(self, code, name, quantity, price):
        item = {
            'code': code,
            'name': name,
            'quantity': quantity,
            'price': price,
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.stock['items'].append(item)
        self.save_stock()
        return "Item added successfully!"

    def remove_item(self, code):
        for i, item in enumerate(self.stock['items']):
            if item['code'] == code:
                del self.stock['items'][i]
                self.save_stock()
                return "Item removed successfully!"
        return "Item not found!"

    def update_quantity(self, code, quantity):
        for item in self.stock['items']:
            if item['code'] == code:
                item['quantity'] = quantity
                item['last_updated'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.save_stock()
                return "Quantity updated successfully!"
        return "Item not found!"

    def list_items(self):
        return self.stock['items']

def main():
    stock = StockControl()
    
    while True:
        print("\n=== Stock Control System ===")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Update Quantity")
        print("4. List Items")
        print("5. Exit")
        
        choice = input("\nChoose an option (1-5): ")
        
        if choice == '1':
            code = input("Enter item code: ")
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            print(stock.add_item(code, name, quantity, price))
            
        elif choice == '2':
            code = input("Enter item code to remove: ")
            print(stock.remove_item(code))
            
        elif choice == '3':
            code = input("Enter item code: ")
            quantity = int(input("Enter new quantity: "))
            print(stock.update_quantity(code, quantity))
            
        elif choice == '4':
            items = stock.list_items()
            if not items:
                print("\nNo items in stock!")
            else:
                print("\nCurrent Stock:")
                print("-" * 70)
                print(f"{'Code':<10} {'Name':<20} {'Quantity':<10} {'Price':<10} {'Last Updated':<20}")
                print("-" * 70)
                for item in items:
                    print(f"{item['code']:<10} {item['name']:<20} {item['quantity']:<10} {item['price']:<10.2f} {item['last_updated']:<20}")
                
        elif choice == '5':
            print("\nThank you for using Stock Control System!")
            break
        
        else:
            print("\nInvalid option! Please try again.")

if __name__ == "__main__":
    main()