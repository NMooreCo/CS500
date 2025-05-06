from models.ItemToPurchase import ItemToPurchase
from models.ShoppingCart import ShoppingCart

def print_menu():
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")   


def is_valid_option(option):
    valid_options = ['a', 'r', 'c', 'i', 'o', 'q']
    return option in valid_options

def get_menu_option():
    print_menu()
    chosen_option = ""
    while not is_valid_option(chosen_option):
        chosen_option = input("Choose an option: ").lower()
        if not is_valid_option(chosen_option):
            print("Invalid option. Please try again.")
    return chosen_option

def get_item_to_add_to_cart():
    item = ItemToPurchase()
    while True:
        try:
            item_name = input("Enter the item name: ")
            if not item_name:
                raise ValueError("Item name cannot be empty.")
            item.item_name = item_name
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            item_description = input("Enter the item description: ")
            if not item_description:
                raise ValueError("Item description cannot be empty.")                
            item.item_description = item_description
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            item_price = input("Enter the item price: ")             
            item.item_price = float(item_price)
            if( item.item_price < 0):
                raise ValueError("Item price cannot be negative.")            
            break
        except ValueError:
            print("Item price must be a number.")

    while True:
        try:
            item_quantity = input("Enter the item quantity: ")
            if not item_quantity.isdigit():
                raise ValueError("Item qty must be a number.")                
            item.item_quantity = int(item_quantity)
            if( item.item_quantity < 0):
                raise ValueError("Item qty cannot be negative.")
            break
        except ValueError as e:
            print(e)
    
    return item

# shopping_cart = ShoppingCart("John Doe", "February 1, 2020")
# item1 = ItemToPurchase("Nike Romaleos", 189, 2, "Volt color, Weightlifting shoes")
# item2 = ItemToPurchase("Chocolate Chips", 3, 5, "Semi-sweet")
# item3 = ItemToPurchase("Powerbeats 2 Headphones", 128, 1, "Bluetooth headphones")
# shopping_cart.add_item(item1)
# shopping_cart.add_item(item2)
# shopping_cart.add_item(item3)

name = input("Enter customer's name: ")
date = input("Enter today's date: ")
shopping_cart = ShoppingCart(name, date)

menu_option = ""
while(menu_option != 'q'):
    menu_option = get_menu_option()
    
    if menu_option == 'a':
        item = get_item_to_add_to_cart()
        shopping_cart.add_item(item)
            
    elif menu_option == 'r':
        item_name = input("Enter name of item to remove: ")
        shopping_cart.remove_item(item_name)
    
    elif menu_option == 'c':
        item_name = input("Enter the item name: ")        
        while True:
            try:
                new_qty = int(input("Enter the new quantity: "))
                if new_qty < 0:
                    raise ValueError("Item quantity cannot be negative.")
                break
            except ValueError as e:
                print(e)
        modified_item = ItemToPurchase(item_name=item_name, item_quantity=int(new_qty))
        shopping_cart.modify_item(modified_item)  
    
    elif menu_option == 'i':
        print("OUTPUT ITEMS' DESCRIPTIONS")
        shopping_cart.print_descriptions()
    
    elif menu_option == 'o':
        print("OUTPUT SHOPPING CART")
        shopping_cart.print_total()
