from shop_functions import load_inventory, save_inventory
from shop_functions import take_order, check_item
from shop_functions import process_sale, show_inventory


print("=== Welcome to Anant's Shop ===")

# Main Program

shop = load_inventory()    # load from file first

item, quantity = take_order()


if check_item(item, shop):
    total_bill = process_sale(item, quantity, shop)
    if total_bill > 0:
        print(f"Total bill: ₹{total_bill}")
    show_inventory(shop)

save_inventory(shop)       # save to file at end
