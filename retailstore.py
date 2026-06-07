import json

print("=== Welcome to Anant's Shop ===")


def load_inventory():
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


def save_inventory(shop):
    with open("shop.json", "w") as file:
        json.dump(shop, file)


def take_order():
    order_item = input("What would you like to order? ").lower()
    quantity = int(input("How many kg? "))
    return order_item, quantity


def check_item(item, shop):
    if item in shop and shop[item]["quantity"] > 0:
        print(f"\n{item} is available!")
        return True

    elif item in shop and shop[item]["quantity"] == 0:
        print(f"\n{item} is out of stock.")
        return False

    else:
        print(f"\n{item} is unavailable.")
        return False


def process_sale(item, quantity_ordered, shop):
    available = shop[item]["quantity"]

    if quantity_ordered <= 0:
        print("Quantity must be greater than 0.")
        return 0

    if quantity_ordered > available:
        print(f"Sorry, only {available} kg available.")
        return 0

    print(f"Price per kg: ₹{shop[item]['price']}")

    total_bill = quantity_ordered * shop[item]["price"]

    shop[item]["quantity"] -= quantity_ordered

    return total_bill


def show_inventory(shop):
    print("\n--- Remaining Inventory ---")

    for item in shop:
        if shop[item]["quantity"] == 0:
            print(f"{item}: OUT OF STOCK")
        else:
            print(f"{item}: {shop[item]['quantity']} kg left")


# Main Program

shop = load_inventory()    # load from file first

item, quantity = take_order()


if check_item(item, shop):
    total_bill = process_sale(item, quantity, shop)
    if total_bill > 0:
        print(f"Total bill: ₹{total_bill}")
    show_inventory(shop)

save_inventory(shop)       # save to file at end
