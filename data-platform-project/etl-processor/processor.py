import requests
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

def fetch_data():
    base_url = "http://fake-data-api:5000"
    
    customers = requests.get(f"{base_url}/customers").json()
    products = requests.get(f"{base_url}/products").json()
    orders = requests.get(f"{base_url}/orders").json()
    
    return customers, products, orders

def save_to_csv(customers, products, orders):
    pd.DataFrame(customers).to_csv('data/customers.csv', index=False)
    pd.DataFrame(products).to_csv('data/products.csv', index=False)
    pd.DataFrame(orders).to_csv('data/orders.csv', index=False)

def save_to_db(customers, products, orders):
    engine = create_engine('postgresql://user:password@db:5432/mydatabase')
    
    pd.DataFrame(customers).to_sql('customers', engine, if_exists='replace', index=False)
    pd.DataFrame(products).to_sql('products', engine, if_exists='replace', index=False)
    pd.DataFrame(orders).to_sql('orders', engine, if_exists='replace', index=False)

def create_visualizations(products, orders):
    # Popular products
    product_counts = pd.DataFrame(orders)['product_id'].value_counts()
    product_names = {p['id']: p['name'] for p in products}
    product_counts.index = product_counts.index.map(product_names)
    
    plt.figure(figsize=(10, 6))
    product_counts.head(10).plot(kind='bar')
    plt.title('Top 10 Popular Products')
    plt.ylabel('Number of Orders')
    plt.tight_layout()
    plt.savefig('data/popular_products.png')
    
    # Sales by category
    product_df = pd.DataFrame(products)
    order_df = pd.DataFrame(orders)
    merged_df = order_df.merge(product_df, left_on='product_id', right_on='id')
    category_sales = merged_df.groupby('category')['quantity'].sum()
    
    plt.figure(figsize=(10, 6))
    category_sales.plot(kind='pie', autopct='%1.1f%%')
    plt.title('Sales by Category')
    plt.ylabel('')
    plt.tight_layout()
    plt.savefig('data/sales_by_category.png')

def main():
    print("Fetching data from API...")
    customers, products, orders = fetch_data()
    
    print("Saving data to CSV...")
    save_to_csv(customers, products, orders)
    
    print("Saving data to database...")
    save_to_db(customers, products, orders)
    
    print("Creating visualizations...")
    create_visualizations(products, orders)
    
    print("ETL process completed!")

if __name__ == "__main__":
    main()