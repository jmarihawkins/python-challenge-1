# Define menu items
menu_items = {
    1: {"Item name": "Apple", "Price": 0.49},
    2: {"Item name": "Tea - Thai iced", "Price": 3.99},
    3: {"Item name": "Fried banana", "Price": 4.49}
}

# Initialize empty order list
order = []

# Function to print menu
def print_menu():
    print("Menu:")
    for key, value in menu_items.items():
        print(f"{key}. {value['Item name']}: ${value['Price']}")

# Function to handle ordering process
def place_order():
    while True:
        # Print menu
        print_menu()
        
        # Get user input for menu selection
        menu_selection = input("Enter your selection: ")

        # Input validation
        if not menu_selection.isdigit():
            print("Error: Please enter a number.")
            continue

        menu_selection = int(menu_selection)

        # Check if menu selection is valid
        if menu_selection not in menu_items.keys():
            print("Error: Invalid selection.")
            continue

        # Get item name
        item_name = menu_items[menu_selection]["Item name"]

        # Get quantity
        quantity_input = input(f"How many {item_name}s would you like? (default is 1): ")
        if not quantity_input.isdigit():
            quantity = 1
        else:
            quantity = int(quantity_input)

        # Add order to the list
        order.append({
            "Item name": item_name,
            "Price": menu_items[menu_selection]["Price"],
            "Quantity": quantity
        })

        # Prompt if the customer wants to continue ordering
        while True:
            choice = input("Would you like to keep ordering? (y/n): ").lower()
            match choice:
                case 'y':
                    break
                case 'n':
                    print("Thank you for your order.")
                    return
                case _:
                    print("Please enter 'y' or 'n'.")

# Function to print receipt
def print_receipt():
    print("Order Receipt:")
    print("Item name                 | Price  | Quantity")
    print("--------------------------|--------|----------")
    total_price = sum(item["Price"] * item["Quantity"] for item in order)
    for item in order:
        item_name = item["Item name"]
        price = item["Price"]
        quantity = item["Quantity"]
        space1 = " " * (27 - len(item_name))
        space2 = " " * (9 - len(str(price)))
        print(f"{item_name}{space1}| ${price}{space2}| {quantity}")
    print("--------------------------|--------|----------")
    print(f"Total: ${total_price}")

# Main function
def main():
    place_order()
    print_receipt()

if __name__ == "__main__":
    main()