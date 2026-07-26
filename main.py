class Item:
    def __init__(self, name: str, cost_price: int, sell_price: int, stock: int):
        self.name = name
        self.cost_price = cost_price
        self.sell_price = sell_price
        self.stock = stock

class Customer:
    def __init__(self, budget: int, wants: list[str]):
        self.budget = budget
        self.wants = wants

class Shop:
    def __init__(self, inventory: list[tuple[Item, int]], cash: int):
        self.inventory = inventory
        self.cash = cash
        self.day = 0

    def restock(self, item: Item, quantity: int):
        # Add stock for an item or create a new inventory entry if needed.
        if item in self.inventory[0]:
            self.inventory[0][item] += quantity
            if self.inventory[0][item] > 20:
                self.inventory[0][item] = 20
        else:
            self.inventory.append((item, quantity))

    def open_for_day(self, customers: list[Customer]):
        # Serve customers by selling matching items if they can afford them.
        for customer in customers:
            for item, quantity in self.inventory:
                if item.name in customer.wants and customer.budget >= item.sell_price and quantity > 0:
                    # sell item to customer
                    self.cash += item.sell_price
                    customer.budget -= item.sell_price
                    self.inventory[self.inventory.index((item, quantity))] = (item, quantity - 1)
                    break  # move to next customer after a purchase

    def end_day(self, rent: int):
        # Deduct daily rent and advance the shop to the next day.
        self.cash -= rent
        self.day += 1

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
    shop.end_day(rent=10)

if __name__ == "__main__":
    main()
