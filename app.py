# Function to add a new item to the inventory
def add_item(inventory):
    item_name = input("Enter the item name to add: ")
    item_quantity = int(input("Enter the item quantity: "))
    
    # Add item to the inventory dictionary
    inventory[item_name] = item_quantity  
    print(f"{item_name} added with quantity {item_quantity}.")

# Function for remove items from the inventory
def remove_item(inventory):
    item_name = input("Enter the item_name to be removed: ")
    if item_name in inventory:
        # Remove the item from the inventory
        del inventory[item_name]  
        print(f"{item_name} has been removed from the inventory.")
    else:
        print(f"{item_name} not found in the inventory.")

# Function for updating the quantity of existing item
def update_item_quantity(inventory):
    item_name = input("Enter the item_name to be updated: ")
    if item_name in inventory:
        # updating items quantity
        new_quantity = int(input("Enter the quantity change (negative to be use for decreasing): "))
        inventory[item_name] += new_quantity  
        print(f"{item_name} quantity updated to {inventory[item_name]}.")
    else:
        print(f"{item_name} not found in the inventory.")

# Function to display all items in the inventory
def show_inventory(inventory):
    print("Current Inventory:")
    for item_name, item_quantity in inventory.items():
        print(f"Item: {item_name}, Quantity: {item_quantity}")

# Main function to run the inventory management system
def main():
    inventory = {}  # Initialize an empty dictionary for holding the inventory
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Update Item Quantity")
        print("4. Show Inventory")
        print("5. Exit")
        
        choice = input("Select an option from (1-5): ")
        
        if choice == "1":
            add_item(inventory)
        elif choice == "2":
            remove_item(inventory)
        elif choice == "3":
            update_item_quantity(inventory)
        elif choice == "4":
            show_inventory(inventory)
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()