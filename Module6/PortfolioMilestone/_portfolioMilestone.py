from models.ItemToPurchase import ItemToPurchase
from models.ShoppingCart import ShoppingCart

def print_menu():
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart total")
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
    
    temp_item = get_item_to_add_to_cart_price_and_qty()
    item.item_price = temp_item.item_price
    item.item_quantity = temp_item.item_quantity
    
    return item

def get_item_to_add_to_cart_price_and_qty():
    item = ItemToPurchase()
    while True:
        try:
            item_price = input("Enter the item price: ")             
            item.item_price = float(item_price)
            break
        except ValueError:
            print("Item price must be a number.")

    while True:
        try:
            item_quantity = input("Enter the item quantity: ")
            if not item_quantity.isdigit():
                raise ValueError("Item qty must be a number.")                
            item.item_quantity = int(item_quantity)
            break
        except ValueError as e:
            print(e)
    
    return item

shopping_cart = ShoppingCart("John Doe", "February 1, 2020")
item1 = ItemToPurchase("Nike Romaleos", 189, 2, "Volt color, Weightlifting shoes")
item2 = ItemToPurchase("Chocolate Chips", 3, 5, "Semi-sweet")
item3 = ItemToPurchase("Powerbeats 2 Headphones", 128, 1, "Bluetooth headphones")
shopping_cart.add_item(item1)
shopping_cart.add_item(item2)
shopping_cart.add_item(item3)

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
    