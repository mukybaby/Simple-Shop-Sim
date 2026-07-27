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