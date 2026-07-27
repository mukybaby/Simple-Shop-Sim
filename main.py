from shop import Shop, Item, Customer

def main():
    # Create some items
    item1 = Item("Widget", 5, 10, 10)
    item2 = Item("Gadget", 3, 6, 15)

    # Create a shop with initial inventory and cash
    shop = Shop(inventory=[(item1, item1.stock), (item2, item2.stock)], cash=100)

    # Create some customers
    customer1 = Customer(budget=20, wants=["Widget"])
    customer2 = Customer(budget=5, wants=["Gadget"])
    customer3 = Customer(budget=15, wants=["Widget", "Gadget"])

    # Open the shop for the day and serve customers
    shop.open_for_day(customers=[customer1, customer2, customer3])

    # Print the final state of the shop
    print(f"Day: {shop.day}, Cash: {shop.cash}")
    for item, quantity in shop.inventory:
        print(f"Item: {item.name}, Stock: {quantity}")

    # End the day with a rent deduction
    print("Ending the day...")
    print(f"Cash before rent: {shop.cash}")
    shop.end_day(rent=10)
    print(f"Cash after rent: {shop.cash}, Day: {shop.day}")

if __name__ == "__main__":
    main()
