## Module 4 - Discussion

What are the key constructs required to create a loop? Identify two scenarios that may require two different types of loops. Be sure to provide specific details for each scenario that illustrate why the different types of loops are required. Include a brief pseudocode example to share that includes at least one loop. Actively participate in this discussion by providing constructive feedback on the scenarios and details posted by your peers.


## Answer

The key constructs requried to create a loop are:

1. Defining the control variable(s) used to create entry/exit condition which is checked/updated each time the loop executes
2. Defining the specific actions that execute each time a loop repeats
3. Defining an appropriate Boolean expression that determines if the loop will be entered and when the loop will stop


Example 1: Using a while loop

I'm currently working on a project that is ingesting massive amounts of documents. 

A while loop with a sliding window is used for the majority of chunking strategies.

For most of the chunking strategies a while loop is used because we do not know the number of repetitions needed to chunk the document when starting the loop. Check for repetitions here is based on if the entire document has been processed. Technically you could accomplish this with a multiple for loops but it would be way less efficient than using a while loop with a sliding window.

``` python
# very simplified fixed length chunking strategy
def simple_fixed_length_chunker(text, chunkSize):
    start_index = 0

    chunks = []
    while start_index < len(text):
        end_index = start_index + chunkSize
        
        if end_index > len(text):
            end_index = len(text)        
        
        chunk = text[start_index:end_index]

        chunks.append(chunk)
        start_index = end_index

    return chunks

chunks = simple_fixed_length_chunker("This is a test string to demonstrate the fixed length chunking strategy.", 10)
print(chunks)
```

Example 2: Using a for loop

I build and automate Mail Order and Central Fill Pharmacies and deal with a fixed number of elements constantly. One example would be recording packing history for specific items in an order once an order is packed. This would use a fixed length loop since the # of prescriptions in the order are fixed. Again like the above example technically you could accomplish this with a while loop but it would require more logic and wouldn't be a easy to understand.

``` python
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
```
