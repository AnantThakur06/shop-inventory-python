from shop_functions import Shop, take_order


print("=== Welcome to Anant's Shop ===")

# Main Program

my_shop = Shop()                    # creates object — __init__ runs, loads inventory
item, quantity = take_order()

if my_shop.check_item(item):        # no need to pass inventory — object knows its own
    total_bill = my_shop.process_sale(item, quantity)
    if total_bill > 0:
        print(f"Total bill: ₹{total_bill}")
    my_shop.show_inventory()

my_shop.save_inventory()
