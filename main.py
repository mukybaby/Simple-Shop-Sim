import json
import random
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
        if shop.loan:
            print(f"The shop has gone negative. The bank has given you a loan of {abs(shop.cash) + 100}. This is the only time the bank will give you a loan.\n")
            shop.cash += abs(shop.cash) + 100
            shop.loan = False
        elif shop.loan == False and shop.cash < 0:
            print(f"The shop has gone negative. The bank has already given you a loan. We are sorry but you have lost the game.\n")
            break

        print(f"Day {shop.day} - Cash: {shop.cash}\n")
        print("What would you like to do?\n")
        print("1. Restock items")

        if shop.open:
            print("2. Serve a customer")
            print("3. Close the shop for the day")
            print("4. Quit\n")

        else:
            print("2. Open for the day")
            print("3. Quit\n")

        if len(shop.customers_in_store) <= 0 and shop.open:
            print("There are no more customers for the day.")

        choice = input("Enter your choice: ")
        print()

        match choice:
            case "1":
                print("  Name  Stock  Price\n")
                for i, item in enumerate(shop.inventory, start=1):
                    print(f"{i} {item.name}  {item.stock}  {item.price}")

                print()

                item_choice = shop.inventory[int(input("Choose an item by name or number: ")) - 1]
                stock_choice = int(input("How much do you want to restock?: "))

                if stock_choice * item_choice.price > shop.cash:
                    print("You dont have enough cash")

                else:
                    shop.cash -= stock_choice * item_choice.price
                    shop.restock(item_choice, stock_choice)

            case "2":
                if shop.open:
                    if len(shop.customers_in_store) > 0:
                        customer = shop.customers_in_store.pop(0)
                        print(f"{customer.name} wants to buy {customer.wants.name} for {customer.wants.price}.")
                        print("Would you like to bargin with them? (Y/n): ")

                        if bargin_choice := input().lower() == "y":
                            chance = random.uniform(0, 100)
                            if customer.bargin_with(chance):
                                print(f"Successfully bargained with {customer.name}! Increased the price by 10%.")
                                customer.wants.price += customer.wants.price * 0.9  # Apply a 10% markup to the price
                            else:
                                print(f"Failed to bargain with {customer.name}. Decreased the price by 10%.")
                                customer.wants.price -= customer.wants.price * 0.1  # Apply a 10% discount to the price
                                customer.buy(customer.wants, shop)
                        elif bargin_choice == "n":
                            customer.buy(customer.wants, shop)

                        else:
                            print("Invalid choice. Please try again.")
                            


                    else:
                        print("There are no more customers for the day.")

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
