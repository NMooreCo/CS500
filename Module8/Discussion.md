# Module 8: Discussion Forum

Briefly describe the difference between a class and an instance of a class. In a Python class, how do you hide an attribute from code outside the class? Provide code examples demonstrating the usage of classes in Python. In response to your peers, provide additional code examples as well as other class differences to build upon the peer postings.

*Be sure to post an initial, substantive response by Thursday at 11:59 p.m. MT, and respond to two or more classmates or the instructor with substantive responses by Sunday at 11:59 p.m. MT.*

***A substantive initial post** answers the question presented completely and/or asks a thoughtful question pertaining to the topic. Be sure your post is unique. Do not repeat what other students have said.*

***Substantive peer responses** ask thoughtful questions pertaining to the topic, and/or answer a question (in detail) posted by another student or the instructor. Note: The following are not examples of substantive contributions:*

- *Thanking, agreeing with, or complimenting a classmate.*
- *Providing irrelevant commentary.*

## Answer
A class is the blueprint or template that defines properties, behavior, and state. An instance of a class is the creation of an object from a class where you can access/use the variables/definitions and maintains state. The difference here is that a class is the definition while an instance of a class is the usage.

You can hide an attribute from code outside the class by prefixing with a double underscore (making it private).

Example:

class Asset:
    def __init__(self, asset, qty):
        self.asset = asset
        self.__qty = qty

    def get_qty(self):
        return self.__qty

    def get_balance(self):
        # Fake out checking asset price
        asset_price = 4.026
        return asset_price * self.__qty

    def sell(self, amount):
        if amount > self.__qty:
            print("Not enough quantity to sell")
            return False
        else:
            self.__qty -= amount
            return True
        
    def buy(self, amount):
        self.__qty += amount
        return True
    

atom = Asset("ATOM", 100)
print("Current qty: ", atom.get_qty())
print("Current balance: ", atom.get_balance())
success = atom.sell(20)
print("Sell success: ", success)
print("Current qty: ", atom.get_qty())
print("Current balance: ", atom.get_balance())
success = atom.sell(100)
print("Sell success: ", success)
print("Current qty: ", atom.get_qty())
print("Current balance: ", atom.get_balance())
success = atom.buy(100)
print("Buy success: ", success)
print("Current qty: ", atom.get_qty()) 