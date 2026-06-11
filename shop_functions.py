import json

class Shop:
    def __init__(self):
        self.inventory = self.load_inventory()

    def load_inventory(self):
        try:
            with open("shop.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {
                "rice":  {"price": 50,  "quantity": 100},
                "dal":   {"price": 80,  "quantity": 50},
                "oil":   {"price": 120, "quantity": 30},
                "sugar": {"price": 45,  "quantity": 75},
                "wheat": {"price": 60,  "quantity": 60}
            }

    def save_inventory(self):
        with open("shop.json", "w") as file:
            json.dump(self.inventory, file)
    
    def show_inventory(self):
        print("\n--- Remaining Inventory ---")
        for item in self.inventory:
            if self.inventory[item]["quantity"] == 0:
             print(f"{item}: OUT OF STOCK")
            else:
             print(f"{item}: {self.inventory[item]['quantity']} kg left")
    
    def check_item(self, item):
        if item in self.inventory and self.inventory[item]["quantity"] > 0:
           print(f"\n{item} is available!")
           return True

        elif item in self.inventory and self.inventory[item]["quantity"] == 0:
           print(f"\n{item} is out of stock.")
           return False

        else:
           print(f"\n{item} is unavailable.")
           return False
    
    def process_sale(self, item, quantity_ordered):
        available = self.inventory[item]["quantity"]

        if quantity_ordered <= 0:
          print("Quantity must be greater than 0.")
          return 0

        if quantity_ordered > available:
          print(f"Sorry, only {available} kg available.")
          return 0

        print(f"Price per kg: ₹{self.inventory[item]['price']}")

        total_bill = quantity_ordered * self.inventory[item]["price"]

        self.inventory[item]["quantity"] -= quantity_ordered

        return total_bill

def take_order():
    order_item = input("What would you like to order? ").lower()
    try:
        quantity = int(input("How many kg? "))
    except ValueError:
        print("Invalid quantity. Setting quantity to 1.")
        quantity = 1
    return order_item, quantity








def show_inventory(self):
        print("\n--- Remaining Inventory ---")
        for item in self.inventory:
            if self.inventory[item]["quantity"] == 0:
             print(f"{item}: OUT OF STOCK")
            else:
             print(f"{item}: {self.inventory[item]['quantity']} kg left")