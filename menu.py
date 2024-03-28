# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# Set up order list
order_list = []

# Launch the store and present a greeting to the customer
print("Welcome to Chef B.R.O.'S Food Truck.")

# Customers may want to order multiple items, so let's create a continuous loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")
    i = 1
    menu_items = {}

    # Print the options to choose from menu headings
    for key in menu.keys():
        print(f"{i}: {key}")
        menu_items[i] = key
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    if menu_category.isdigit():
        if int(menu_category) in menu_items.keys():
            menu_category_name = menu_items[int(menu_category)]
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1

            menu_item_number = input("Enter the item number: ")
            if menu_item_number.isdigit():
                menu_item_number = int(menu_item_number)
                if menu_item_number in menu_items.keys():
                    item_name = menu_items[menu_item_number]["Item name"]
                    quantity = input(f"How many {item_name} would you like to order? ")
                    if quantity.isdigit():
                        quantity = int(quantity)
                    else:
                        quantity = 1

                    order_list.append({
                        "Item name": item_name,
                        "Price": menu_items[menu_item_number]["Price"],
                        "Quantity": quantity
                    })

                    print(f"{quantity} {item_name}(s) added to your order.")
                else:
                    print("Invalid item number.")
            else:
                print("You didn't select a valid item number.")

        else:
            print("Invalid menu number.")
    else:
        print("You didn't select a number.")

    while True:
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o: ")

        if keep_ordering.upper() == "Y":
            break
        elif keep_ordering.upper() == "N":
            place_order = False
            break
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

# Print out the customer's order
print("This is what we are preparing for you.\n")
print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# Loop through the items in the customer's order and print
total_cost = 0
for item in order_list:
    item_name = item["Item name"]
    price = item["Price"]
    quantity = item["Quantity"]
    print(f"{item_name.ljust(26)}| ${price:.2f} | {quantity}")
    total_cost += price * quantity

# Print the total cost
print(f"\nTotal cost: ${total_cost:.2f}")

# Print a thank you message
print("Thank You! Come Again!")