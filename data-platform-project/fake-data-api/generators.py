from faker import Faker
import csv
import json
import random

fake = Faker()

def generate_customers(num=100):
    customers = []
    for i in range(num):
        customers.append({
            'id': i + 1,
            'name': fake.name(),
            'email': fake.email(),
            'address': fake.address(),
            'phone': fake.phone_number()
        })
    return customers

def generate_products(num=50):
    products = []
    categories = ['Electronics', 'Clothing', 'Books', 'Home & Kitchen', 'Sports']
    for i in range(num):
        products.append({
            'id': i + 1,
            'name': fake.word().capitalize() + ' ' + fake.word(),
            'price': round(random.uniform(5, 500), 2),
            'category': random.choice(categories)
        })
    return products

def generate_orders(num=200):
    orders = []
    for i in range(num):
        orders.append({
            'id': i + 1,
            'customer_id': random.randint(1, 100),
            'product_id': random.randint(1, 50),
            'quantity': random.randint(1, 5),
            'order_date': fake.date_this_year()
        })
    return orders