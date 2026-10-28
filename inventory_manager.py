import json
import os

class Product:
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = float(price)
        self.__stock = int(stock)

    @property
    def product_id(self):
        return self.__product_id

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def stock(self):
        return self.__stock

    def update_stock(self, quantity: int -> None):
        self.__stock = quantity

    def display_information(self) -> None:
            """Displays formatted information for the product."""
            print(f"ID: {self.__product_id} | Name: {self.__name} | Price: ${self.__price:.2f} | Stock: {self.__stock}")
    
    def to_dict(self):
        """Convert Product object back to a dictionary for JSON storage."""
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Product object from a dictionary loaded from JSON."""
        return cls(data["id"], data["name"], data["price"], data["stock"])


class InventoryManager:
    def __init__(self, filename="inventory.json"):
        self.filename = filename
        self.inventory = []
        self.load_inventory()

    def load_inventory(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                print(f"{self.filename} found.")
                print("Inventory loaded successfully.\n")
                data = json.load(file)
                self.inventory = [Product.from_dict(item) for item in data]
        else:
            print(f"{self.filename} not found. Starting with empty inventory.\n")
            self.inventory = []

    def save_inventory(self):
        print("Saving inventory...")
        data = [product.to_dict() for product in self.inventory]
        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Inventory saved successfully to {self.filename}.\n")

    def display_all(self):
        print("Current Inventory")
        print("-" * 45)
        if not self.inventory:
            print("No products in inventory.")
        else:
            for item in self.inventory:
                item.display_information()
        print("-" * 45)
        print()

    def add_product(self):
        print("Add new product")
        product_id = input("Product ID: ").strip()
        name = input("Product Name: ").strip()

        try:
            price = float(input("Price: "))
            stock = int(input("Stock Quantity: "))
        except ValueError:
            print("Invalid price or stock input. Product not added.\n")
            return

        new_product = Product(product_id, name, price, stock)
        self.inventory.append(new_product)
        print("\nProduct added successfully!\n")

    def update_stock(self):
        print("Update Stock")
        product_id = input("Enter Product ID: ").strip()
        print()

        for item in self.inventory:
            if item.product_id.lower() == product_id.lower():
                print("Product Found:")
                print(f"Name: {item.name}")
                print(f"Current Stock: {item.stock}\n")
                try:
                    new_stock = int(input("New Stock Quantity: "))
                    item.update_stock(new_stock) # Using the class method
                    print("\nStock updated successfully!\n")
                    return
                except ValueError:
                    print("Invalid stock quantity input\n")
                    return

        print("Product not found.\n")

    def search_product(self):
        print("Search Product")
        query = input("Enter Product ID: ").strip()
        print()

        for item in self.inventory:
            if item.product_id.lower() == query.lower():
                print("Product Found")
                print("-" * 45)
                item.display_information()
                print("-" * 45 + "\n")
                return

        print("Product not found.\n")


def display_menu():
    print("=" * 35)
    print("INVENTORY MANAGEMENT SYSTEM (OOP)")
    print("=" * 35)
    print()


def main():
    display_menu()
    manager = InventoryManager()

    while True:
        print("--------MENU--------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("--------------------\n")

        option = input("Enter option: ").strip()
        print()

        if option == "1":
            manager.display_all()
        elif option == "2":
            manager.add_product()
        elif option == "3":
            manager.update_stock()
        elif option == "4":
            manager.search_product()
        elif option == "5":
            manager.save_inventory()
        elif option == "6":
            print("Saving inventory before exit...")
            manager.save_inventory()
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else: 
            print("Invalid option. Please try again.\n")


if __name__ == "__main__":
    main()