class ShoppingCart:
    def __init__(self):
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def print_cart_total(self):
        total_cost = 0
        print("TOTAL COST")
        for item in self.cart_items:
            item.print_item_cost()
            total_cost += item.item_price * item.item_quantity
        print(f"Total: ${total_cost:.2f}")