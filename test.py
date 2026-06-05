def greet(name):
    print(f"Hello {name}! Welcome to Python learning.")
greet("Anant")
greet("Lucky")
greet("Harish")

def calculate_total(price, quantity ):
    total_bill = price * quantity
    return total_bill
total_cost = calculate_total(50, 3)
total_cost = calculate_total(80, 2)
print(f"Total cost: ₹{total_cost}")


def check_stock(quantity):
    if quantity > 0:
        return "In stock"
    else:
        return "Out of stock"
item_availiable = check_stock(5)
item_availiable = check_stock(0)
print(item_availiable)

shop = {
    "rice":  {"price": 50,  "quantity": 10},
    "dal":   {"price": 80,  "quantity": 0},
    "oil":   {"price": 120, "quantity": 5}
}

def process_order(item, shop):
    if item in shop and shop[item]["quantity"] > 0:
        print(f'{item} is available and price : ₹{shop[item]["price"]}')
        return True
    elif item in shop and shop[item]["quantity"] == 0:
        print(f"{item} is out of stock")
        return False
    else:
        print(f"{item} is unavailable")
        return False
process_order("rice", shop)    # available
process_order("dal", shop)     # out of stock
process_order("pizza", shop)   # unavailable


def mystery(x):
    if x > 10:
        return "big"
    return "small"

print(mystery(15)) # big
print(mystery(5)) # small
print(mystery(10)) # small x should be greater than 10 not equal 