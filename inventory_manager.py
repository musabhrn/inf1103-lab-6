import json
import os

FILENAME = "inventory.json"

def load_inventory():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            print(f"{FILENAME} found.")
            print("Inventory loaded successfully.\n")
            return json.load(file)
    else:
        print(f"{FILENAME} not found. Starting with empty inventory.\n")
        return []

def save_inventory(inventory):
    print("Saving inventory...")
    with open(FILENAME, "w") as file:
        json.dump(inventory, file, indent=4)
    print(f"Inventory saved successfully to {FILENAME}.\n")

def display_all(inventory):
    print("Current Inventory")
    print("-" * 45)
    if not inventory:
        print("No products in inventory.")
    else:
        for item in inventory:
            print(
                f"ID: {item['id']} | Name: {item['name']} | Price: ${item['price']:.2f} | Stock: {item['stock']}"
            )
    print("-" * 45)
    print()

def add_product(inventory):
    print("Add new product")
    product_id = input("Product ID: ").strip()
    name = input("Product Name: ").strip()

    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))

    new_product = {
        "id": product_id,
        "name": name,
        "price": price,
        "stock": stock
    }

    inventory.append(new_product)
    print("\nProduct added successfully!\n")

def update_stock (inventory):
    print("Update Stock")
    product_id = input("Enter Product ID: ").strip()
    print()

    for item in inventory:
        if item['id'].lower() == product_id.lower():
            print("Product Found:")
            print(f"Name: {item['name']}")
            print(f"Current Stock: {item['stock']}\n")
            try:
                new_stock = int(input("New Stock Quantity: "))
                item['stock'] = new_stock
                print("\nStock updated successfully!\n")
                return
            except ValueError:
                print("Invalid stock quantity input\n")
                return

    print("Product not found.\n")

def search_product(inventory):
    print("Search Product")
    query = input("Enter Product ID: ").strip()
    print()

    for item in inventory:
        if item['id'].lower() == query.lower():
            print("Product Found")
            print("-" * 45)
            print(f"ID: {item['id']}")
            print(f"Name: {item['name']}")
            print(f"Price: {item['price']}")
            print(f"Stock: {item['stock']}")
            print("-" * 45 + "\n")
            return

    print("Product not found.\n")


def display_menu():
    print("=" * 35)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 35)
    print()

def main():
    display_menu()
    inventory = load_inventory()

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
            display_all(inventory)
        elif option == "2":
            add_product(inventory)
        elif option == "3":
            update_stock(inventory)
        elif option == "4":
            search_product(inventory)
        elif option == "5":
            save_inventory(inventory)
        elif option == "6":
            print("Saving inventory before exit...")
            with open(FILENAME, "w") as file:
                json.dump(inventory, file, indent=4)
            print("Inventory saved successfully.\n")
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else: 
            print("Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()