from models.ItemToPurchase import ItemToPurchase
from models.ShoppingCart import ShoppingCart

cart = ShoppingCart()
for i in range(2):
    print(f"Item {i+1}")
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

    cart.add_item(item)

cart.print_cart_total()