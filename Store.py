class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price} dollars."

class Store:
    def __init__(self, name, serial_number):
        self.name = name
        self.serial_number = serial_number
        self.products = []

    def add_product(self, product):
        if isinstance(product, Product):
            self.products.append(product)
            print(f"{product.name} added to {self.name}.")
        else:
            print("Invalid product!")

    def __delete_product(self, product):
        self.products.remove(product)

    def print_products(self):
        print(f"Products in {self.name}:")
        for product in self.products:
            print(f"- {product}")

class Buyer:
    def __init__(self, first_name, last_name, available_funds):
        self.first_name = first_name
        self.last_name = last_name
        self.available_funds = available_funds

    def __str__(self):
        return f"{self.first_name} {self.last_name} - Available funds: {self.available_funds} dollars."

    def buy_product(self, product, store):
        if product in store.products and self.available_funds >= product.price:
            self.available_funds -= product.price
            store._Store__delete_product(product)  # Fix here
            print(f"{self.first_name} bought {product.name} from {store.name}.")
        elif product in store.products and self.available_funds < product.price:
            print(f"{self.first_name} does not have enough funds to buy {product.name}.")
        else:
            print(f"{product.name} is not available in {store.name}.")

product1 = Product("Laptop", 3000)
product2 = Product("TV", 2000)
product3 = Product("Smartphone", 1500)
product4 = Product("Mouse", 500)
product5 = Product("Keyboard", 1000)

store1 = Store("StoreTech", "12345")
store2 = Store("Electronics", "67890")

store1.add_product(product1)
store1.add_product(product2)
store1.add_product(product3)

store2.add_product(product4)
store2.add_product(product5)

buyer1 = Buyer("Bojana", "Vasilevska", 3000)
buyer2 = Buyer("Cica", "Maca", 1000)


store1.print_products()
store2.print_products()

buyer1.buy_product(product1, store1)
buyer1.buy_product(product4, store2)

print(buyer1)
print(buyer2)