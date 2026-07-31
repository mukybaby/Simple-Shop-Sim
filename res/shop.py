import random

class Item:
    def __init__(self, name: str, price: int, stock: int):
        self.name = name
        self.price = price
        self.stock = stock

class Customer:
	def __init__(self ,name: str ,budget: int, wants: Item):
		self.name = name
		self.budget = budget
		self.wants = wants

class Shop:
    def __init__(self, name: str, inventory: list[tuple[Item, int]], cash: int):
        self.name = name
        self.inventory: list[Item] = inventory
        self.cash = cash
        self.day = 1
        self.open = False
        self.customers_in_store: list[Customer] = []

    def restock(self, item: Item, quantity: int):
        # Add stock for an item or create a new inventory entry if needed.
        if item in self.inventory:
             for item_check in self.inventory:
                  if item_check == item:   
                    item_check.stock += quantity
        else:
            print(f'"{item.name}" is not in invotory')

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