# Overview

This code is essentially a simple program for managing orders in a menu-based system, similar to what you might find in a restaurant or café.

# Menu Definition
At the beginning, the code defines a menu_items dictionary. This dictionary contains various items available for ordering, each item identified by a number. For each item, its name and price are listed.

# Order Management
The program then initializes an empty list called 'order' to keep track of the items ordered by the user.

# Functions:

print_menu(): This function displays the menu to the user, listing all the items along with their respective numbers and prices.
place_order(): This function handles the ordering process. It continuously prompts the user to select items from the menu, input the quantity desired, and adds the selected items to the order list.
print_receipt(): Once the user finishes placing the order, this function generates a receipt summarizing the items ordered, their prices, quantities, and the total cost.
main(): This is the main function that orchestrates the order placement and receipt printing process.

# Ordering Process

The 'place_order()' function repeatedly displays the menu and prompts the user to select items by entering the corresponding numbers.
It validates user input to ensure it's a number and corresponds to a valid menu item.
After selecting an item, the user can specify the quantity desired.
The selected item along with its price and quantity are added to the 'order' list.
The user is then asked if they want to continue ordering. If not, the order process stops, and the receipt is printed.

# Receipt Generation

The 'print_receipt()' function formats and prints out the order details neatly, including each item's name, price, quantity, and the total cost of the order.

# Execution

The 'main()' function is called to start the ordering process and generate the receipt.

In summary, this code facilitates a simple ordering system where users can choose items from a menu, specify quantities, and receive a receipt detailing their order and total cost.
