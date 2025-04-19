# simple message queue using a list to store messages with a simple producer-consumer model
messages = []

def send_message(message):
    # simulate sending a message by appending it to the messages list
    messages.append(message)
    print(f"Message sent: {message}")

def receive_messages():
    # simulate receiving a message by popping it from the messages list
    # process messages until none are left
    while messages:
        message = messages.pop(0)
        print(f"Message received: {message}")

send_message("Examples message 1")
receive_messages()
send_message("Examples message 2")
send_message("Examples message 3")
send_message("Examples message 4")
receive_messages()