# record packed order history for all items in an order
def record_packed_order_history(order_number):
    item_ids = get_items_ids_in_order(order_number)
    for item_id in item_ids:
        record_item_packed_order_history(item_id)
    print(f"Packed order history recorded for order number: {order_number}")

def get_items_ids_in_order(order_number):    
    return [123456789, 112233445, 9867654321,]

def record_item_packed_order_history(item_id):    
    print(f"Recording packed item hisotry for item_id: {item_id}")

record_packed_order_history(11111111)
