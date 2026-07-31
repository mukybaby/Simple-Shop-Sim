import json
from res.shop import Shop, Item, Customer, make_customers

def main():
    with open("res/customer_names.json") as f:
        customer_names = json.load(f)


    print("Welcome to the shop!")
    shop = Shop(input("What do you want to name your shop?: "), [], 100)
    print()
    with open("res/items.json") as f:
        for item in json.load(f):
            shop.inventory.append(Item(item[0], item[1], 5))

    while True:
        print("What would you like to do?\n")
        print("1. Restock items")
        if shop.open:
            print("2. Serve a customer")
            print("3. Close the shop for the day")
            print("4. Quit\n")
        else:
            print("2. Open for the day")
            print("3. Quit\n")

        choice = input("Enter your choice: ")
        print()

        match choice:
            case "1":
                print("  Name  Stock  Price\n")
                for i, item in enumerate(shop.inventory, start=1):
                    print(f"{i} {item.name}  {item.stock}  {item.price}")
                print()
                choice = input("Choose an item by name or number: ")
                stock_choice = int(input("How much do you want to restock?: "))
                if stock_choice > shop.cash:
                    print("You dont have enough cash")
                else:
                    shop.cash -= stock_choice * item.price
                    shop.restock(shop.inventory[int(choice) - 1], stock_choice)

            case "2":
                if shop.open:
                    # Serve Customer
                    pass
                else:
                    shop.open_for_day(make_customers(shop.day, shop, customer_names))
                    print(f"{shop.name} is now open for the day!\n")
                    for customer in shop.customers_in_store:
                        print(customer.name)
                    print("These are the customers for the day.\n")
            case "3":
                if shop.open:
                    shop.end_day(shop.day * 10)
                else:
                    print("Thanks for playing!")
                    break
            case "4":
                if shop.open:
                    print("Thanks for playing!")
                    break
                else:
                    print("Invalid choice. Please try again.")
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
