class Asset:
    def __int__(self, asset, qty):
        self.asset = asset
        self.__qty = qty

    def get_qty(self):
        self.__qty

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
        
