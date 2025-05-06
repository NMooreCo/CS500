from models.ItemToPurchase import ItemToPurchase

class ShoppingCart:
    def __init__(self, name = "none", current_date = "January 1, 2020"):        
        self.cart_items = []
        self.customer_name = name
        self.current_date = current_date
        print("Customer name: ", self.customer_name)
        print("Today's date: ", self.current_date)

    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)

    def remove_item(self, item_to_remove):
        for item in self.cart_items:
            if item.item_name == item_to_remove:
                self.cart_items.remove(item)
                break
        else:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, modified_item):
        for item in self.cart_items:
            if item.item_name == modified_item.item_name:
                if modified_item.item_price != 0:
                    item.item_price = modified_item.item_price
                if modified_item.item_quantity != 0:
                    item.item_quantity = modified_item.item_quantity
                if modified_item.item_description != "none":
                    item.item_description = modified_item.item_description
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_items = 0
        for item in self.cart_items:
            total_items += item.item_quantity
        return total_items
    
    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost
    
    def print_total(self):        
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        if len(self.cart_items) <= 0:
            print("SHOPPING CART IS EMPTY")
            return
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        for item in self.cart_items:
            item.print_item_cost()
        print(f"Total: ${self.get_cost_of_cart():.2f}")        


    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")

    def print_cart_total(self):
        total_cost = 0
        print("TOTAL COST")
        for item in self.cart_items:
            item.print_item_cost()
            total_cost += item.item_price * item.item_quantity
        print(f"Total: ${total_cost:.2f}")