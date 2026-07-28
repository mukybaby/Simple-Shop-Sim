import random

class Item:
    def __init__(self, name: str, sell_price: int, stock: int):
        self.name = name
        self.sell_price = sell_price
        self.stock = stock

class Customer:
	def __init__(self ,name: str ,budget: int, wants: Item):
		self.name = name
		self.budget = budget
		self.wants = wants

class Shop:
    def __init__(self, name: str, inventory: list[tuple[Item, int]], cash: int):
        self.name = name
        self.inventory: list[tuple[Item, int]] = inventory
        self.cash = cash
        self.day = 1
        self.open = False
        self.customers_in_store: list[Customer] = []

    def restock(self, item: Item, quantity: int):
        # Add stock for an item or create a new inventory entry if needed.
        for index, (inv_item, inv_quantity) in enumerate(self.inventory):
            if inv_item.name == item.name:
                self.inventory[index] = (inv_item, min(inv_quantity + quantity, 20))
                return
        self.inventory.append((item, min(quantity, 20)))

    def open_for_day(self, customers: list[Customer]):
        # Serve customers by selling matching items if they can afford them.
        self.open = True
        for customer in customers:
            self.customers_in_store.append(customer)


    def end_day(self, rent: int):
        # Deduct daily rent and advance the shop to the next day.
        self.open = False
        self.cash -= rent
        self.day += 1


def make_customers(day: int, shop: Shop, customers_name: list[str]) -> list[Customer]:
	total_customers = day * 3
	customers: list[Customer] = []
	while len(customers) != total_customers:
		new_customer = Customer(random.choice(customers_name), random.randint(17, 286), random.choice(shop.inventory))
		customers.append(new_customer)
	return customers