class Item:
    def __init__(self, name, cost_price, sell_price, stock):
        self.name = name
        self.cost_price = cost_price
        self.sell_price = sell_price
        self.stock = stock

class Customer:
    def __init__(self, budget, wants):
        self.budget = budget
        self.wants = wants

class Shop:
    def __init__(self, inventory: list[tuple[Item, int]], cash: int):
        self.inventory = inventory
        self.cash = cash
        self.day = 0

    def restock(self, item_name: str, quantity: int):
        pass

    def open_for_day(self, customers: list[Customer]):
        # generate customers, run sales
        pass

    def end_day(self, rent: int):
        # pay rent, advance day
        pass
