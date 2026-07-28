from shop import Shop, Item, Customer

def main():
    print("Welcome to the shop!")
    shop = Shop(input("What do you want to name your shop?: "), [], 100)

    while True:
        print("What would you like to do?")
        print("1. Restock items")
        if shop.open:
            print("2. Open for the day (Shop is currently open)")
        print("2. Open for the day")
        print("3. End the day")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Implement restock functionality
            pass
        elif choice == "2":
            # Implement open for the day functionality
            pass
        elif choice == "3":
            # Implement end the day functionality
            pass
        elif choice == "4":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
