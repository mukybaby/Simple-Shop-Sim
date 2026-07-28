import json
from res.shop import Shop, Item, Customer, make_customers

def main():
    with open("res/customer_names.json") as f:
        customer_names = json.load(f)


    print("Welcome to the shop!")
    shop = Shop(input("What do you want to name your shop?: "), [], 100)
    with open("res/items.json") as f:
        for item in json.load(f):
            shop.inventory.append(Item(item[0], item[1], 5))

    while True:
        print("What would you like to do?")
        print("1. Restock items")
        if shop.open:
            print("2. Serve a customer")
            print("3. Close the shop for the day")
            print("4. Quit")
        else:
            print("2. Open for the day")
            print("3. Quit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                # Implement restock functionality
                pass
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
