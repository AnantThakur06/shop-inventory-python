class Shop:
    def __init__(self):
        self.inventory = {}   

    def show_inventory(self):
        print("\n--- Remaining Inventory ---")
        for item in self.inventory:
            if self.inventory[item]["quantity"] == 0:
             print(f"{item}: OUT OF STOCK")
            else:
             print(f"{item}: {self.inventory[item]['quantity']} kg left")