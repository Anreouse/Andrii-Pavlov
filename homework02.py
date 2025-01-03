class Product:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price  # ціна товару
        self.description = description  # опис товару
        self.dimensions = dimensions  # габарити товару

    def __str__(self):
        return f"Товар: {self.name}, Ціна: {self.price} грн, Опис: {self.description}, Габарити: {self.dimensions}"


class Customer:
    def __init__(self, surname, name, patronymic, phone):
        self.surname = surname  # прізвище
        self.name = name  # ім'я
        self.patronymic = patronymic  # по батькові
        self.phone = phone  # мобільний телефон

    def __str__(self):
        return f"Покупець: {self.surname} {self.name} {self.patronymic}, Телефон: {self.phone}"


class Order:
    def __init__(self, customer):
        self.customer = customer  # покупець
        self.products = {}  # словник для зберігання товарів і їх кількості

    def add_product(self, product, quantity):
        if product in self.products:
            self.products[product] += quantity
        else:
            self.products[product] = quantity

    def total_cost(self):
        return sum(product.price * quantity for product, quantity in self.products.items())

    def __str__(self):
        products_str = "\n".join(
            [f"{product.name} - Кількість: {quantity}" for product, quantity in self.products.items()])
        total = self.total_cost()
        return f"Замовлення для {self.customer}\nТовари:\n{products_str}\nСумарна вартість: {total} грн"


# Створення екземплярів класу Product
product1 = Product("Ноутбук", 20000, "Сучасний ноутбук для роботи та розваг", "35x24x2 см")
product2 = Product("Смартфон", 10000, "Новий смартфон з великою батареєю", "15x7x0.8 см")

# Створення екземплярів класу Customer
customer1 = Customer("Іваненко", "Іван", "Іванович", "+380501234567")

# Створення замовлення
order1 = Order(customer1)
order1.add_product(product1, 1)  # Додаємо 1 ноутбук
order1.add_product(product2, 2)  # Додаємо 2 смартфони

# Виведення інформації про замовлення
print(order1)